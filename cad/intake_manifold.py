"""
07K -> ZN6 (RWD, upright) short-runner intake manifold, v1.
Generates STEP solids with CadQuery. Run:  python3 cad/intake_manifold.py

Layout (engine upright, flywheel to the rear):
  X  along the engine, cylinder 1 at the X=0 end of the flange file  (ASSUMPTION - see CYL1_AT_ORIGIN)
  Y  outboard from the head face (the flange back face is at Y = FLANGE_T)
  Z  up (the tabbed edge of the flange with the centre lug is the top)
Throttle body on the FRONT end cap, facing forward (-X), for a front-mount intercooler.

All dimensions mm.
"""
import math, os, sys
import cadquery as cq

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- parameters
HEAD_FLANGE_STEP = os.path.join(HERE, "inputs", "07k_flange.STEP")
CYL1_AT_ORIGIN   = True     # True: cylinder 1 (belt end, FRONT of the car) is at the X=0 end of the flange file. VERIFY.
FLANGE_T         = 16.0     # 5/8 in plate
BOLT_HOLE_D      = 6.6      # clearance for the M6 intake bolts

RUNNER_OD        = 57.15    # 2.25 in tube
RUNNER_WALL      = 1.65     # 0.065 in
RUNNER_L         = 150.0    # flange back face -> plate front face (the main packaging knob)
TRANSITION_L     = 40.0     # length over which the hammered tube end goes oval -> round
CB_DEPTH         = 2.0      # counterbore depth that locates each tube for welding

PLATE_T          = 16.0     # runner plate (welded to the runners; the plenum bolts to it)
PLATE_H          = 100.0
PLATE_L          = 460.0
BELL_R           = 8.0      # radiused runner entry machined into the plate
ORING_CS         = 3.53     # -2xx series O-ring cross-section
GROOVE_W, GROOVE_D = 4.6, 2.7
PLATE_BOLT_D     = 5.0      # tap drill for M6 in the runner plate

PLENUM_FLANGE_T  = 8.0      # plate welded to the plenum tube, bolts to the runner plate
PLENUM_OD        = 101.6    # 4 in tube
PLENUM_WALL      = 3.175    # 0.125 in
PLENUM_L         = 440.0
PLENUM_FLAT_W    = 60.0     # width of the flat milled on the tube where the flange plate welds on

ENDCAP_T         = 6.0
TB_PLATE_T       = 12.0
TB_PLATE_W       = 110.0
TB_BORE          = 64.0     # stock 07K throttle body 07K133062A/B
TB_BOLT_SQUARE   = 76.0     # PLACEHOLDER - measure the stock TB bolt pattern
TB_BOLT_D        = 6.6

INJ_BUNG_OD, INJ_BUNG_L = 19.0, 25.0                   # weld-in injector bung, 3/4 in OD x 1 in
INJ_SEAT_D, INJ_SEAT_DEPTH, INJ_THRU_D = 14.0, 10.0, 11.0  # 14 mm lower O-ring seat, then through-bore
INJ_ANGLE_DEG    = 30.0     # bung axis vs the runner axis
INJ_Y_FROM_FACE  = 50.0     # where the bung axis crosses the runner top wall, from the flange back face

BUNG_SMALL = dict(od=15.9, h=12.7, bore=8.7)       # Vibrant 11170, 1/8-27 NPT: 5/8 in OD, tap drill 11/32 in
BUNG_LARGE = dict(od=25.4, h=19.0, bore=14.7)      # Vibrant 11172, 3/8-18 NPT: 1 in OD, tap drill 37/64 in (brake booster)

# ---------------------------------------------------------------- head flange from the user's STEP
src = cq.importers.importStep(HEAD_FLANGE_STEP).solids().vals()[0]
face = max((f for f in src.Faces() if f.geomType() == "PLANE" and abs(f.normalAt().y + 1) < 0.01), key=lambda f: f.Area())
outer = face.outerWire()
ports, bolt_pts = [], []
for w in face.innerWires():
    es = w.Edges()
    if len(es) <= 2 and all(e.geomType() == "CIRCLE" for e in es):
        c = w.Center(); bolt_pts.append((c.x, c.z))
    else:
        ports.append(w)
ports.sort(key=lambda w: w.Center().x)
PORT_X = [w.Center().x for w in ports]
PORT_Z = ports[0].Center().z
bb = ports[0].BoundingBox()
PORT_W, PORT_H = bb.xlen, bb.zlen                        # 61.4 x 38.9 obround at the head face
X_MID = (PORT_X[0] + PORT_X[-1]) / 2

# crushed-tube obround: same perimeter as the round tube
def obround_for_perimeter(P, h):
    return (P - math.pi * h) / 2 + h                      # width for height h
TUBE_P_OD = math.pi * RUNNER_OD
TUBE_P_ID = math.pi * (RUNNER_OD - 2 * RUNNER_WALL)
CB_H = PORT_H + 2 * RUNNER_WALL + 0.6                     # outer obround height at the flange (0.3 mm clearance per side)
CB_W = obround_for_perimeter(TUBE_P_OD, CB_H)
ID_H = CB_H - 2 * RUNNER_WALL
ID_W = obround_for_perimeter(TUBE_P_ID, ID_H)

# flange solid: user's outline + ports, extruded to FLANGE_T, with fresh M6 clearance holes
flange = cq.Workplane("XY").add(cq.Solid.extrudeLinear(outer, ports, cq.Vector(0, FLANGE_T, 0)))
def xz_cut(x, z, y0, depth, maker):
    """cut a prism from y0 (toward +Y by depth) at X,Z on an XZ workplane"""
    wp = cq.Workplane("XZ", origin=(0, y0 + depth, 0)).center(x, z)
    return maker(wp).extrude(depth)                       # XZ normal is -Y, so extrude(+) goes from y0+depth down to y0
for (x, z) in bolt_pts:
    flange = flange.cut(xz_cut(x, z, 0, FLANGE_T, lambda wp: wp.circle(BOLT_HOLE_D / 2)))
for x in PORT_X:                                          # obround counterbores on the back face
    flange = flange.cut(xz_cut(x, PORT_Z, FLANGE_T - CB_DEPTH, CB_DEPTH, lambda wp: wp.slot2D(CB_W, CB_H)))

# ---------------------------------------------------------------- runners
Y_FL = FLANGE_T
Y_PL = FLANGE_T + RUNNER_L                                # plate front face
def runner(x):
    y0 = Y_FL - CB_DEPTH
    # outer: obround -> round loft, then straight tube into the plate counterbore
    o1 = (cq.Workplane("XZ", origin=(0, y0, 0)).center(x, PORT_Z).slot2D(CB_W, CB_H)
          .workplane(offset=-TRANSITION_L).circle(RUNNER_OD / 2).loft())
    o2 = (cq.Workplane("XZ", origin=(0, y0 + TRANSITION_L, 0)).center(x, PORT_Z).circle(RUNNER_OD / 2)
          .extrude(-(RUNNER_L - TRANSITION_L + 2 * CB_DEPTH)))
    i1 = (cq.Workplane("XZ", origin=(0, y0 - 1, 0)).center(x, PORT_Z).slot2D(ID_W, ID_H)
          .workplane(offset=-(TRANSITION_L + 1)).circle(RUNNER_OD / 2 - RUNNER_WALL).loft())
    i2 = (cq.Workplane("XZ", origin=(0, y0 + TRANSITION_L, 0)).center(x, PORT_Z).circle(RUNNER_OD / 2 - RUNNER_WALL)
          .extrude(-(RUNNER_L + 10)))
    return o1.union(o2).cut(i1).cut(i2)
runners = [runner(x) for x in PORT_X]

# injector bungs on top of each runner, aimed at the port
def injector_bung(x):
    th = math.radians(INJ_ANGLE_DEG)
    d = cq.Vector(0, math.cos(th), math.sin(th))         # outward direction (away from the head, upward)
    # the axis crosses the runner's top wall here
    y_wall = Y_FL + INJ_Y_FROM_FACE
    z_wall = PORT_Z + (ID_H / 2 + RUNNER_WALL if INJ_Y_FROM_FACE < TRANSITION_L else RUNNER_OD / 2)
    start = cq.Vector(x, y_wall, z_wall) - d * 12         # start inside the runner, then trim to its surface
    tip = start + d * (INJ_BUNG_L + 12)                   # outer (fuel rail) end of the bung
    bung = cq.Workplane("XY").add(cq.Solid.makeCylinder(INJ_BUNG_OD / 2, INJ_BUNG_L + 12, start, d))
    # trim the base to the runner's outer surface (round section here)
    bung = bung.cut(cq.Workplane("XZ", origin=(0, y_wall + 60, 0)).center(x, PORT_Z).circle(RUNNER_OD / 2).extrude(120))
    seat = cq.Solid.makeCylinder(INJ_SEAT_D / 2, INJ_SEAT_DEPTH + 1, tip - d * INJ_SEAT_DEPTH, d)
    chamfer = cq.Solid.makeCone(INJ_SEAT_D / 2, INJ_SEAT_D / 2 + 1.5, 1.5, tip - d * 1.5, d)
    thru = cq.Solid.makeCylinder(INJ_THRU_D / 2, INJ_BUNG_L + 50, tip - d * (INJ_BUNG_L + 40), d)
    bore = cq.Workplane("XY").add(seat).union(cq.Workplane("XY").add(chamfer)).union(cq.Workplane("XY").add(thru))
    return bung, bore
inj_bungs, inj_bores = zip(*[injector_bung(x) for x in PORT_X])
runners = [r.cut(b) for r, b in zip(runners, inj_bores)]
inj_bungs = [b.cut(br) for b, br in zip(inj_bungs, inj_bores)]

# ---------------------------------------------------------------- runner plate (welded to the runners)
RID = RUNNER_OD - 2 * RUNNER_WALL
plate = (cq.Workplane("XZ", origin=(0, Y_PL + PLATE_T, 0)).center(X_MID, PORT_Z)
         .rect(PLATE_L, PLATE_H).extrude(PLATE_T))
for x in PORT_X:
    plate = plate.cut(xz_cut(x, PORT_Z, Y_PL, CB_DEPTH, lambda wp: wp.circle(RUNNER_OD / 2 + 0.2)))   # tube seat
    plate = plate.cut(xz_cut(x, PORT_Z, Y_PL, PLATE_T, lambda wp: wp.circle(RID / 2)))               # through
plate = plate.faces(">Y").edges("%CIRCLE").fillet(BELL_R)                                             # bell-mouth entries
# bolt pattern (M6 tapped) and O-ring groove on the plenum side
BX = [X_MID - PLATE_L / 2 + 8] + [X_MID + dx for dx in (-176, -88, 0, 88, 176)] + [X_MID + PLATE_L / 2 - 8]
BZ = [PORT_Z - PLATE_H / 2 + 8, PORT_Z + PLATE_H / 2 - 8]
BOLTS = [(x, z) for x in BX for z in BZ]
for (x, z) in BOLTS:
    plate = plate.cut(xz_cut(x, z, Y_PL, PLATE_T, lambda wp: wp.circle(PLATE_BOLT_D / 2)))
G_OUT_L, G_OUT_H = PLATE_L - 36, PLATE_H - 30            # groove centreline rectangle
groove = (cq.Workplane("XZ", origin=(0, Y_PL + PLATE_T, 0)).center(X_MID, PORT_Z)
          .rect(G_OUT_L + GROOVE_W, G_OUT_H + GROOVE_W).extrude(GROOVE_D)
          .cut(cq.Workplane("XZ", origin=(0, Y_PL + PLATE_T, 0)).center(X_MID, PORT_Z)
               .rect(G_OUT_L - GROOVE_W, G_OUT_H - GROOVE_W).extrude(GROOVE_D)))
plate = plate.cut(groove)

# ---------------------------------------------------------------- plenum flange plate (welded to the tube)
Y_PF = Y_PL + PLATE_T                                     # plenum flange front face = runner plate back face
pflange = (cq.Workplane("XZ", origin=(0, Y_PF + PLENUM_FLANGE_T, 0)).center(X_MID, PORT_Z)
           .rect(PLATE_L, PLATE_H).extrude(PLENUM_FLANGE_T))
for x in PORT_X:
    pflange = pflange.cut(xz_cut(x, PORT_Z, Y_PF, PLENUM_FLANGE_T, lambda wp: wp.circle(RID / 2)))
for (x, z) in BOLTS:
    pflange = pflange.cut(xz_cut(x, z, Y_PF, PLENUM_FLANGE_T, lambda wp: wp.circle(TB_BOLT_D / 2)))

# ---------------------------------------------------------------- plenum tube with a milled flat
R = PLENUM_OD / 2
sag = R - math.sqrt(R ** 2 - (PLENUM_FLAT_W / 2) ** 2)   # depth of the flat
Y_AX = Y_PF + PLENUM_FLANGE_T + (R - sag)                 # tube axis
X0 = X_MID - PLENUM_L / 2
tube = (cq.Workplane("YZ", origin=(X0, Y_AX, PORT_Z)).circle(R).circle(R - PLENUM_WALL).extrude(PLENUM_L))
flat_cut = (cq.Workplane("XY", origin=(X_MID, Y_PF + PLENUM_FLANGE_T - 20, PORT_Z))
            .box(PLENUM_L + 2, 20, PLENUM_OD + 2, centered=(True, False, True)))   # removes everything below the flat (Y < flange back face)
tube = tube.cut(flat_cut)
front_x = X0 if CYL1_AT_ORIGIN else X0 + PLENUM_L         # throttle body goes on the cylinder-1 end

# end profile (circle minus the flat) for the rear cap
def end_profile(x, t, sign):
    cap = cq.Workplane("YZ", origin=(x, Y_AX, PORT_Z)).circle(R).extrude(sign * t)
    return cap.cut(cq.Workplane("XY", origin=(x, Y_PF + PLENUM_FLANGE_T - 20, PORT_Z))
                   .box(2 * t + 2, 20, PLENUM_OD + 2, centered=(True, False, True)))
rear_x = X0 + PLENUM_L if CYL1_AT_ORIGIN else X0
rear_cap = end_profile(rear_x, ENDCAP_T, 1 if CYL1_AT_ORIGIN else -1)

# throttle body adapter plate on the front end
tb_sign = -1 if CYL1_AT_ORIGIN else 1
tb_plate = (cq.Workplane("YZ", origin=(front_x, Y_AX, PORT_Z)).rect(TB_PLATE_W, TB_PLATE_W).extrude(tb_sign * TB_PLATE_T)
            .faces(">X" if tb_sign < 0 else "<X").workplane().hole(TB_BORE))
for dy in (-1, 1):
    for dz in (-1, 1):
        tb_plate = tb_plate.cut(cq.Workplane("YZ", origin=(front_x - (TB_PLATE_T + 1 if tb_sign < 0 else 1), Y_AX + dy * TB_BOLT_SQUARE / 2, PORT_Z + dz * TB_BOLT_SQUARE / 2))
                                .circle(TB_BOLT_D / 2).extrude(TB_PLATE_T + 2))
# trim the TB plate to the flat side (it must not stick below the flange plate line)
tb_plate = tb_plate.cut(cq.Workplane("XY", origin=(front_x, Y_PF + PLENUM_FLANGE_T - 30, PORT_Z))
                        .box(2 * TB_PLATE_T + 4, 30, PLENUM_OD + 20, centered=(True, False, True)))
# open the tube end into the TB bore (the tube is already open-ended) - nothing to cut

# ---------------------------------------------------------------- NPT bungs on top of the plenum
def bung(x, spec):
    top_z = PORT_Z + R
    b = cq.Workplane("XY", origin=(x, Y_AX, top_z - 4)).circle(spec["od"] / 2).extrude(spec["h"] + 4)
    # seat the bung on the curved tube surface
    b = b.cut(cq.Workplane("YZ", origin=(x - spec["od"], Y_AX, PORT_Z)).circle(R).extrude(2 * spec["od"]))
    hole = cq.Workplane("XY", origin=(x, Y_AX, top_z - PLENUM_WALL - 2)).circle(spec["bore"] / 2).extrude(spec["h"] + 10)
    return b.cut(hole), hole
bung_specs = [(X_MID - 150, BUNG_SMALL), (X_MID - 75, BUNG_SMALL), (X_MID, BUNG_LARGE), (X_MID + 75, BUNG_SMALL), (X_MID + 150, BUNG_SMALL)]
bungs = []
for x, spec in bung_specs:
    b, hole = bung(x, spec); bungs.append(b); tube = tube.cut(hole)

# ---------------------------------------------------------------- export
parts = {
    "01_head_flange": flange,
    "02_runner_plate": plate,
    "03_plenum_flange": pflange,
    "04_plenum_tube": tube,
    "05_rear_cap": rear_cap,
    "06_tb_adapter": tb_plate,
}
for i, r in enumerate(runners): parts[f"10_runner_{i+1}"] = r
for i, b in enumerate(inj_bungs): parts[f"20_injector_bung_{i+1}"] = b
for i, b in enumerate(bungs): parts[f"30_npt_bung_{i+1}"] = b

asm = cq.Assembly(name="07K_RWD_intake")
for name, p in parts.items():
    cq.exporters.export(p, os.path.join(OUT, f"{name}.step"))
    asm.add(p, name=name)
asm.save(os.path.join(OUT, "00_assembly.step"))

# one merged body for Flow Simulation (lids go on the TB bore and the five port faces)
shapes = [flange.val()] + [r.val() for r in runners] + [plate.val(), pflange.val(), tube.val(), rear_cap.val(), tb_plate.val()] + [b.val() for b in inj_bungs] + [b.val() for b in bungs]
merged_shape = shapes[0].fuse(*shapes[1:], glue=False).clean()
merged = cq.Workplane("XY").add(merged_shape)
print(f"merged body: {len(merged.solids().vals())} solid(s) (should be 1)")
cq.exporters.export(merged, os.path.join(OUT, "00_merged_for_flowsim.step"))
cq.exporters.export(merged, os.path.join(OUT, "00_merged_preview.stl"), tolerance=0.2, angularTolerance=0.2)

# ---------------------------------------------------------------- report
vol_plenum = math.pi * (R - PLENUM_WALL) ** 2 * PLENUM_L / 1e6
print(f"ports: {len(PORT_X)} obround {PORT_W:.1f} x {PORT_H:.1f} on {PORT_X[1]-PORT_X[0]:.1f} mm centres, X = {[round(x,1) for x in PORT_X]}")
print(f"crushed tube end: outer obround {CB_W:.1f} x {CB_H:.1f}, inner {ID_W:.1f} x {ID_H:.1f}  (port {PORT_W:.1f} x {PORT_H:.1f})")
print(f"runner ID {RID:.1f} mm, length {RUNNER_L} mm; plate at Y={Y_PL:.0f}; plenum axis at Y={Y_AX:.0f}, Z={PORT_Z:.1f}; outermost Y = {Y_AX+R:.0f} mm from the head face")
print(f"plenum {PLENUM_OD} OD x {PLENUM_L} long = {vol_plenum:.2f} L (1.0-1.4 L/L target for 2.5 L: {vol_plenum/2.5:.2f})")
print(f"throttle body ({TB_BORE} mm) at X={front_x:.0f} facing {'-X (front)' if CYL1_AT_ORIGIN else '+X'}")
mb = merged.val().BoundingBox()
print(f"overall envelope: X {mb.xmin:.0f}..{mb.xmax:.0f}, Y {mb.ymin:.0f}..{mb.ymax:.0f}, Z {mb.zmin:.0f}..{mb.zmax:.0f}")
print("wrote", len(parts) + 2, "STEP files to", OUT)
