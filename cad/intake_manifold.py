"""
07K -> ZN6 (RWD, upright) short-runner intake manifold, v2: sheet-metal box plenum.
Generates STEP solids (and DXF flat patterns) with CadQuery.  Run:  python3 cad/intake_manifold.py

Layout (engine upright, flywheel to the rear):
  X  along the engine, cylinder 1 at the X=0 end of the flange file  (ASSUMPTION - see CYL1_AT_ORIGIN)
  Y  outboard from the head face (the flange back face is at Y = FLANGE_T)
  Z  up (the tabbed edge of the flange with the centre lug is the top)
Throttle body on the FRONT end plate, facing forward (-X), for a front-mount intercooler.

Construction (all 6061 / 5052 aluminium, TIG with 4043):
  head flange   16 mm plate, your outline, obround counterbores for the hammered tube ends     (Haas)
  runners x5    2.25 in x 0.065 tube, straight, head end crushed oval                           (press / vise)
  floor         8 mm plate: runners weld into counterbored holes; bell-mouth radius inside       (Haas)
  top wall, bottom wall, roof   3 mm sheet, welded at the corners (or fold the three as one U)  (shear + brake)
  front end     12 mm plate = the throttle body flange (64 mm bore)                             (Haas)
  rear end      3 mm sheet
  bungs         Vibrant NPT weld bungs on the top wall; EV14 weld-in injector bungs on the runners
All dimensions mm.
"""
import math, os
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
RUNNER_L         = 150.0    # flange back face -> plenum floor (the main packaging knob)
TRANSITION_L     = 40.0     # length over which the hammered tube end goes oval -> round
CB_DEPTH         = 2.0      # counterbore depth that locates each tube for welding

FLOOR_T          = 8.0      # plenum floor plate (runners weld into it)
BELL_R           = 5.0      # radiused runner entry machined into the floor
BOX_L            = 440.0    # plenum length along the engine (outside)
BOX_H            = 110.0    # plenum height in Z (outside)
D_FRONT          = 90.0     # plenum depth outboard at the throttle-body end (outside, from the floor's inner face)
D_REAR           = 65.0     # ... at the rear end (taper helps end-entry distribution; set equal for no taper)
SHEET_T          = 3.0      # 1/8 in sheet for walls and roof
FRONT_PLATE_T    = 12.0     # the throttle body flange
REAR_PLATE_T     = 3.0

TB_BORE          = 64.0     # stock 07K throttle body 07K133062A/B
TB_BOLT_SQUARE   = 76.0     # PLACEHOLDER - measure the stock TB bolt pattern
TB_BOLT_D        = 5.0      # tap drill for M6

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

def obround_for_perimeter(P, h):                          # crushed tube keeps its perimeter
    return (P - math.pi * h) / 2 + h
CB_H = PORT_H + 2 * RUNNER_WALL + 0.6
CB_W = obround_for_perimeter(math.pi * RUNNER_OD, CB_H)
ID_H = CB_H - 2 * RUNNER_WALL
ID_W = obround_for_perimeter(math.pi * (RUNNER_OD - 2 * RUNNER_WALL), ID_H)
RID = RUNNER_OD - 2 * RUNNER_WALL

def xz_cut(x, z, y0, depth, maker):
    """prism from y0 to y0+depth at (x,z); XZ workplane normal is -Y so extrude(+) runs toward -Y"""
    return maker(cq.Workplane("XZ", origin=(0, y0 + depth, 0)).center(x, z)).extrude(depth)

flange = cq.Workplane("XY").add(cq.Solid.extrudeLinear(outer, ports, cq.Vector(0, FLANGE_T, 0)))
for (x, z) in bolt_pts:
    flange = flange.cut(xz_cut(x, z, 0, FLANGE_T, lambda wp: wp.circle(BOLT_HOLE_D / 2)))
for x in PORT_X:
    flange = flange.cut(xz_cut(x, PORT_Z, FLANGE_T - CB_DEPTH, CB_DEPTH, lambda wp: wp.slot2D(CB_W, CB_H)))

# ---------------------------------------------------------------- runners
Y_FL = FLANGE_T
Y_FLOOR = FLANGE_T + RUNNER_L                             # floor plate, runner side
def runner(x):
    y0 = Y_FL - CB_DEPTH
    o1 = (cq.Workplane("XZ", origin=(0, y0, 0)).center(x, PORT_Z).slot2D(CB_W, CB_H)
          .workplane(offset=-TRANSITION_L).circle(RUNNER_OD / 2).loft())
    o2 = (cq.Workplane("XZ", origin=(0, y0 + TRANSITION_L, 0)).center(x, PORT_Z).circle(RUNNER_OD / 2)
          .extrude(-(RUNNER_L - TRANSITION_L + 2 * CB_DEPTH)))
    i1 = (cq.Workplane("XZ", origin=(0, y0 - 1, 0)).center(x, PORT_Z).slot2D(ID_W, ID_H)
          .workplane(offset=-(TRANSITION_L + 1)).circle(RID / 2).loft())
    i2 = (cq.Workplane("XZ", origin=(0, y0 + TRANSITION_L, 0)).center(x, PORT_Z).circle(RID / 2)
          .extrude(-(RUNNER_L + 10)))
    return o1.union(o2).cut(i1).cut(i2)
runners = [runner(x) for x in PORT_X]

def injector_bung(x):
    th = math.radians(INJ_ANGLE_DEG)
    d = cq.Vector(0, math.cos(th), math.sin(th))         # outward, away from the head and upward
    y_wall = Y_FL + INJ_Y_FROM_FACE
    z_wall = PORT_Z + RUNNER_OD / 2
    start = cq.Vector(x, y_wall, z_wall) - d * 12
    tip = start + d * (INJ_BUNG_L + 12)
    bung = cq.Workplane("XY").add(cq.Solid.makeCylinder(INJ_BUNG_OD / 2, INJ_BUNG_L + 12, start, d))
    bung = bung.cut(cq.Workplane("XZ", origin=(0, y_wall + 60, 0)).center(x, PORT_Z).circle(RUNNER_OD / 2).extrude(120))
    seat = cq.Solid.makeCylinder(INJ_SEAT_D / 2, INJ_SEAT_DEPTH + 1, tip - d * INJ_SEAT_DEPTH, d)
    chamfer = cq.Solid.makeCone(INJ_SEAT_D / 2, INJ_SEAT_D / 2 + 1.5, 1.5, tip - d * 1.5, d)
    thru = cq.Solid.makeCylinder(INJ_THRU_D / 2, INJ_BUNG_L + 50, tip - d * (INJ_BUNG_L + 40), d)
    bore = cq.Workplane("XY").add(seat).union(cq.Workplane("XY").add(chamfer)).union(cq.Workplane("XY").add(thru))
    return bung, bore
inj_bungs, inj_bores = zip(*[injector_bung(x) for x in PORT_X])
runners = [r.cut(b) for r, b in zip(runners, inj_bores)]

# ---------------------------------------------------------------- plenum: floor plate
X0 = X_MID - BOX_L / 2                                    # front end of the box (cyl-1 end if CYL1_AT_ORIGIN)
X1 = X0 + BOX_L
Y_IN = Y_FLOOR + FLOOR_T                                  # inside face of the floor
floor = (cq.Workplane("XZ", origin=(0, Y_IN, 0)).center(X_MID, PORT_Z).rect(BOX_L, BOX_H).extrude(FLOOR_T))
for x in PORT_X:
    floor = floor.cut(xz_cut(x, PORT_Z, Y_FLOOR, CB_DEPTH, lambda wp: wp.circle(RUNNER_OD / 2 + 0.2)))  # tube seat
    floor = floor.cut(xz_cut(x, PORT_Z, Y_FLOOR, FLOOR_T, lambda wp: wp.circle(RID / 2)))              # through
floor = floor.faces(">Y").edges("%CIRCLE").fillet(BELL_R)                                              # bell-mouths

# ---------------------------------------------------------------- walls and roof (3 mm sheet)
def depth_at(x):                                          # outside depth from the floor's inner face
    t = (x - X0) / BOX_L
    return D_FRONT + (D_REAR - D_FRONT) * (t if CYL1_AT_ORIGIN else 1 - t)
# top / bottom walls: trapezoids in the XY plane, 3 mm thick in Z, sitting on the floor's inner face
def side_wall(z_outer, sign):
    pts = [(X0, Y_IN), (X1, Y_IN), (X1, Y_IN + depth_at(X1) - SHEET_T), (X0, Y_IN + depth_at(X0) - SHEET_T)]
    return cq.Workplane("XY", origin=(0, 0, z_outer - (SHEET_T if sign > 0 else 0))).polyline(pts).close().extrude(SHEET_T)
Z_TOP = PORT_Z + BOX_H / 2
Z_BOT = PORT_Z - BOX_H / 2
top_wall = side_wall(Z_TOP, +1)
bot_wall = side_wall(Z_BOT, -1)
# roof: sloped flat plate covering the wall tops, full Z width
roof_pts = [(X0, Y_IN + depth_at(X0) - SHEET_T), (X1, Y_IN + depth_at(X1) - SHEET_T), (X1, Y_IN + depth_at(X1)), (X0, Y_IN + depth_at(X0))]
roof = cq.Workplane("XY", origin=(0, 0, Z_BOT)).polyline(roof_pts).close().extrude(BOX_H)

# ---------------------------------------------------------------- end plates
def end_plate(x_face, t, sign, d_here):
    """plate inside the U: spans the inner Z width and the inner depth; sign = +1 grows toward +X"""
    w = cq.Workplane("YZ", origin=(x_face, 0, 0)).center(Y_IN + (d_here - SHEET_T) / 2, PORT_Z).rect(d_here - SHEET_T, BOX_H - 2 * SHEET_T)
    return w.extrude(sign * t)
if CYL1_AT_ORIGIN:
    front_plate = end_plate(X0, FRONT_PLATE_T, +1, depth_at(X0)); rear_plate = end_plate(X1, REAR_PLATE_T, -1, depth_at(X1))
    TB_X, TB_SIGN = X0, -1
else:
    front_plate = end_plate(X1, FRONT_PLATE_T, -1, depth_at(X1)); rear_plate = end_plate(X0, REAR_PLATE_T, +1, depth_at(X0))
    TB_X, TB_SIGN = X1, +1
TB_YC = Y_IN + (depth_at(TB_X) - SHEET_T) / 2             # throttle body centre
tb_cut = cq.Workplane("YZ", origin=(TB_X + TB_SIGN * 1, 0, 0)).center(TB_YC, PORT_Z).circle(TB_BORE / 2).extrude(-TB_SIGN * (FRONT_PLATE_T + 2))
front_plate = front_plate.cut(tb_cut)
for dy in (-1, 1):
    for dz in (-1, 1):
        h = (cq.Workplane("YZ", origin=(TB_X + TB_SIGN * 1, 0, 0)).center(TB_YC + dy * TB_BOLT_SQUARE / 2, PORT_Z + dz * TB_BOLT_SQUARE / 2)
             .circle(TB_BOLT_D / 2).extrude(-TB_SIGN * (FRONT_PLATE_T + 2)))
        front_plate = front_plate.cut(h)

# ---------------------------------------------------------------- NPT bungs on the top wall
def bung(x, spec):
    yc = Y_IN + (depth_at(x) - SHEET_T) / 2
    b = cq.Workplane("XY", origin=(x, yc, Z_TOP)).circle(spec["od"] / 2).extrude(spec["h"])
    hole = cq.Workplane("XY", origin=(x, yc, Z_TOP - SHEET_T - 1)).circle(spec["bore"] / 2).extrude(spec["h"] + 2)
    return b.cut(hole), hole
bung_specs = [(X_MID - 150, BUNG_SMALL), (X_MID - 75, BUNG_SMALL), (X_MID, BUNG_LARGE), (X_MID + 75, BUNG_SMALL), (X_MID + 150, BUNG_SMALL)]
bungs = []
for x, spec in bung_specs:
    b, hole = bung(x, spec); bungs.append(b); top_wall = top_wall.cut(hole)

# ---------------------------------------------------------------- export
parts = {
    "01_head_flange": flange, "02_floor_plate": floor, "03_top_wall": top_wall, "04_bottom_wall": bot_wall,
    "05_roof": roof, "06_front_plate_TB": front_plate, "07_rear_plate": rear_plate,
}
for i, r in enumerate(runners): parts[f"10_runner_{i+1}"] = r
for i, b in enumerate(inj_bungs): parts[f"20_injector_bung_{i+1}"] = b
for i, b in enumerate(bungs): parts[f"30_npt_bung_{i+1}"] = b
for f in os.listdir(OUT):
    if f.endswith((".step", ".dxf", ".stl")): os.remove(os.path.join(OUT, f))
asm = cq.Assembly(name="07K_RWD_intake_v2")
for name, p in parts.items():
    cq.exporters.export(p, os.path.join(OUT, f"{name}.step")); asm.add(p, name=name)
asm.save(os.path.join(OUT, "00_assembly.step"))
shapes = [p.val() for p in parts.values()]
merged = cq.Workplane("XY").add(shapes[0].fuse(*shapes[1:], glue=False).clean())
cq.exporters.export(merged, os.path.join(OUT, "00_merged_for_flowsim.step"))
cq.exporters.export(merged, os.path.join(OUT, "00_merged_preview.stl"), tolerance=0.2, angularTolerance=0.2)

# DXF flat patterns for the shear / laser (2D, mm)
def dxf(name, wp): cq.exporters.exportDXF(wp, os.path.join(OUT, f"flat_{name}.dxf"))
dxf("floor_plate", cq.Workplane("XY").rect(BOX_L, BOX_H).extrude(1).faces(">Z").workplane()
    .pushPoints([(x - X_MID, 0) for x in PORT_X]).circle(RID / 2).cutThruAll().faces(">Z"))
for nm in ("top_wall", "bottom_wall"):
    dxf(nm, cq.Workplane("XY").polyline([(0, 0), (BOX_L, 0), (BOX_L, depth_at(X1) - SHEET_T), (0, depth_at(X0) - SHEET_T)]).close().extrude(1).faces(">Z"))
roof_len = math.hypot(BOX_L, depth_at(X1) - depth_at(X0))
dxf("roof", cq.Workplane("XY").rect(roof_len, BOX_H).extrude(1).faces(">Z"))
dxf("front_plate_TB", cq.Workplane("XY").rect(depth_at(TB_X) - SHEET_T, BOX_H - 2 * SHEET_T).extrude(1).faces(">Z").workplane()
    .circle(TB_BORE / 2).cutThruAll().faces(">Z").workplane().rect(TB_BOLT_SQUARE, TB_BOLT_SQUARE, forConstruction=True).vertices().circle(TB_BOLT_D / 2).cutThruAll().faces(">Z"))
dxf("rear_plate", cq.Workplane("XY").rect(depth_at(X1 if CYL1_AT_ORIGIN else X0) - SHEET_T, BOX_H - 2 * SHEET_T).extrude(1).faces(">Z"))

# ---------------------------------------------------------------- report
vol = (BOX_H - 2 * SHEET_T) * ((depth_at(X0) + depth_at(X1)) / 2 - SHEET_T) * (BOX_L - FRONT_PLATE_T - REAR_PLATE_T) / 1e6
R_in, T = 3.0, SHEET_T
BA = math.pi / 2 * (R_in + 0.4 * T); BD = 2 * (R_in + T) - BA
print(f"merged body: {len(merged.solids().vals())} solid(s) (should be 1)")
print(f"ports: 5 obround {PORT_W:.1f} x {PORT_H:.1f} on {PORT_X[1]-PORT_X[0]:.1f} mm centres")
print(f"crushed tube end: outer obround {CB_W:.1f} x {CB_H:.1f}, inner {ID_W:.1f} x {ID_H:.1f}")
print(f"runner ID {RID:.1f}, length {RUNNER_L}; floor at Y={Y_FLOOR:.0f}; box {BOX_L} x {BOX_H} x {D_FRONT}->{D_REAR} deep; plenum {vol:.2f} L ({vol/2.5:.2f} x displacement)")
print(f"outermost point: Y = {Y_IN + D_FRONT:.0f} mm from the head face; throttle body ({TB_BORE} mm) at X={TB_X:.0f} facing {'front (-X)' if TB_SIGN < 0 else '+X'}")
print(f"if you fold top wall + roof + bottom wall as one U from {T} mm sheet, inside radius {R_in}: bend deduction {BD:.1f} mm per bend -> flat width = 2 x wall + {BOX_H} - {2*BD:.1f} (bend a test strip first)")
mb = merged.val().BoundingBox()
print(f"overall envelope: X {mb.xmin:.0f}..{mb.xmax:.0f}, Y {mb.ymin:.0f}..{mb.ymax:.0f}, Z {mb.zmin:.0f}..{mb.zmax:.0f}")
print("wrote", len(parts) + 2, "STEP files and 6 DXF flat patterns to", OUT)
