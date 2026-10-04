# 07K Swap Planning — Chat Notes

*Conversation of October 4, 2026. Organized by topic in the order it was discussed. Prices are approximate and were current at the time; CAD unless marked USD.*

---

## Contents

1. [MK4 2.5 (07K) swap — cost and difficulty](#1-mk4-25-07k-swap--cost-and-difficulty)
2. [Comparing the two swap guides](#2-comparing-the-two-swap-guides)
3. [Finding a rust-free MK4 and importing from the US](#3-finding-a-rust-free-mk4-and-importing-from-the-us)
4. [AWD MK4?](#4-awd-mk4)
5. [Golf R / RS3 five-cylinder dream](#5-golf-r--rs3-five-cylinder-dream)
6. [Other 07K swap platforms (and the E46)](#6-other-07k-swap-platforms-and-the-e46)
7. [The decision: turbo 07K ZN6](#7-the-decision-turbo-07k-zn6)
8. [ECU strategy](#8-ecu-strategy)
9. [Transmission](#9-transmission)
10. [Turbo and manifold](#10-turbo-and-manifold)
11. [Cost vs a K24 swap](#11-cost-vs-a-k24-swap)
12. [Design philosophy: make vs buy](#12-design-philosophy-make-vs-buy)
13. [Flywheel, clutch and the bellhousing stack-up](#13-flywheel-clutch-and-the-bellhousing-stack-up)
14. [Oil pan](#14-oil-pan)
15. [Adapter design and CAD sources](#15-adapter-design-and-cad-sources)
16. [Open items](#16-open-items)
17. [Sources](#17-sources)

---

## 1. MK4 2.5 (07K) swap — cost and difficulty

Started from a TikTok guide (ihatemqb) for swapping a VW 2.5 inline-five into a MK4 Jetta/Golf.

### Cost estimate (CAD)

| Item | Estimate |
|---|---|
| Manual 2.0 MK4 (already has an 02J trans) | $2,500–4,000 (e.g. 2007 Jetta City 2.0 5-spd listed at $4,000 OBO) |
| 2.5 engine with ECU + harness | $500–2,000 (eBay ~US$1,150; the guide's $300 was a lucky deal) |
| Beetle harness, mounts, coolant flanges/hoses | $500–900 |
| Clutch/flywheel + starter | $600–1,000 |
| Exhaust manifold + custom exhaust | $300–700 |
| Swap file (RevMap) | US$140–195, +$20 MK4 pedal support, +$35 immobilizer removal |
| Fluids, gaskets, block-offs, terminals, surprises | $500+ |

- **Swap parts:** ~$3,000–5,500
- **All-in with the car:** ~$6,000–9,000 (more if you need a hoist/engine stand)
- **Payoff:** ~170 hp vs the 2.0's ~115 hp

### Difficulty: medium
- VW-to-VW with the factory ECU; Beetle shares the MK4 platform so mounts bolt in.
- **Bellhousing shave:** the MK4 trans bell and the newer 2.5 block interfere slightly (Fabless confirms). Trial-fit repeatedly — overdoing it can crack the timing cover.
- **ECU re-pinning:** RevMap's free "Charles" tool compares chassis and 2.5 pinouts and highlights changed pins.
- **Front end / lock carrier removal:** tedious, not hard.
- **Biggest real hurdle:** logistics — garage, hoist, a car that can sit dead for weeks.

### Watch out for
- **Rust:** Ontario MK4s rot (rear arches, rockers). A clean shell matters most.
- **Emissions:** the swap file removes SAI, N80 (EVAP) and rear O2 functions (RevMap labels it off-road). On a plated car that's emissions tampering. Tell your insurer about the swap regardless.

---

## 2. Comparing the two swap guides

Second guide: wilkie.cole (Instagram). Core content matches; differences are mostly options.

| Topic | ihatemqb (TikTok) | wilkie.cole (Instagram) |
|---|---|---|
| ECU wiring | Move pin 21 → pin 23 (relay 428 switched ground); new pin 21 wire to fused source hot at start/run; pin 3 to constant 12V (term. 30) or key won't shut engine off | Same |
| Engine year | 2008–2014; 2010+ engine on older Beetle harness needs Beetle oil filter housing (w/ relief valve), screw-in oil pressure switch, 4-pin coolant temp sensor | "Any year" (less precise) |
| ECU | Used RevMap swap file | 2006–2010 Beetle harness + ECU, or ME7.1.1 Rabbit/Jetta ECU + swap tune |
| Transmission | 02J (1.8T/1.9/2.0); shave bellhousing | 02J, 02M 6-speed, or the Beetle 2.5's own box (no shaving) |
| Trans mount | Beetle trans mount | MK4 trans mount + dogbone, MK4 axles |
| Power steering / A/C | Strongly recommends hydraulic PS 2.5 | Hydraulic PS bracket keeps A/C; MK4-style relocation bracket replaces the A/C compressor |
| Cooling, fuel, exhaust, deletes | Covered (Beetle flanges/hoses, returnless fuel, 4-bar filter, SAI block-offs, vacuum pump delete, MK5/MK6 manifold, T14 green wire extension to rain tray) | Not covered |

**Takeaway:** use ihatemqb's as the main checklist, wilkie's for extra trans/A/C options. Verify pin moves against RevMap's pinout tool for your exact ECU.

---

## 3. Finding a rust-free MK4 and importing from the US

### Where to look
- **Closest reliably clean region:** US Southeast — NC, SC, TN, GA. Raleigh/Charlotte ≈ 13–15 h from Ottawa (vs BC ≈ 4,500 km).
- **Skip:** Virginia, Maryland, Pennsylvania (still salt).
- **Non-runners** ("blown motor", "bad trans") are ideal since you're swapping anyway. Clean titles only — salvage titles are hard to import.
- **Ontario options:** search "Krown", "oil sprayed", "summer car", "garage kept"; Ontario VW Facebook groups; flippers selling "southern car / Texas car / rust-free".
- **Check underneath even on southern cars** (many migrate from the rust belt). Expect sun damage instead.

### Rust: walk away vs fixable
- **Walk away:** rotted frame rails or floor pans, crumbling jack points/rockers, rust at rear beam or subframe mounts.
- **Fixable:** rear wheel arch rust (cheap repair panels), surface rust on rockers/door bottoms.

### Importing
- **RIV:** every MK4 is 15+ years old → exempt from the RIV program.
- **US export:** AES filing must be accepted ≥72 h before crossing; acceptance can take up to 24 h → plan ~4 business days. You can buy remotely, file, then fly down after the clock runs.
- **Taxes:** 5% GST at the border + Ontario's 8% portion; $100 A/C excise tax.
- **Duty:** VIN starting with **3** (Mexico, most Jettas) → duty-free under CUSMA; **W** (Germany) or **9** (Brazil) → 6.1%.
- **Reality check:** the 13% is the same as an Ontario private sale. Example: US$2,500 Jetta ≈ $3,560 CAD at ~1.42 → ~$565 in taxes vs ~$465 on an equivalent private sale. Import-specific extra ≈ $100 (+ duty if non-Mexican).
- **Real costs:** exchange rate, getting it home, export filing service fee.

### Getting it home
- Fly/bus one-way and drive it back; bring a friend; or ship it (only option for a non-runner).
- Sort insurance and a temporary/transit plate before buying.
- Closest crossing to Ottawa: Ogdensburg–Prescott (export paperwork goes to that specific port).

### Buying from a dealer
- **Ontario dealer that imported it:** already through customs, usually safetied; 13% HST same as private; OMVIC all-in pricing and disclosure of out-of-province history/branding. Downside: markup.
- **US dealer:** clean title, temp tag to drive out; some handle export filing/shipping (ask up front); ask about waiving state sales tax for export.

---

## 4. AWD MK4?

- MK4s are almost all FWD. AWD exceptions: **Golf R32** (2004, 3.2 VR6, Haldex), **Jetta wagon 4Motion** (2.8 VR6), Euro-only 4Motion Golfs.
- **Converting FWD → AWD with OEM parts is possible but big:**
  - Cut and weld in a 4Motion rear floor pan section (FWD floor lacks mounts)
  - Rear subframe, multi-link suspension, Haldex diff, fuel tank, full MK4 4Motion driveshaft (MK5 parts won't fit)
  - 02M 4Motion trans from an **Audi TT quattro** (R32's 02M has a VR6 bellhousing)
  - Haldex control — usually a standalone controller
- **Decision:** no AWD.

---

## 5. Golf R / RS3 five-cylinder dream

- Crashed MK8 Golf Rs aren't rare — IAA lists dozens of Golf Rs, including 2022–2025 MK8s.
- **Turbo 07K is the wrong five for MQB:** custom everything, and MQB's ABS/DSG/rear diff expect torque data from a factory MQB ECU.
- **The version that works:** Audi RS3's **2.5 TFSI** (same MQB platform). Done many times in MK7 Rs using a crashed RS3 donor (engine, DQ500 DSG, RS3 rear end) with essentially no fabrication — one shop does it in ~5 weeks. VW asked Audi for the 2.5 for the MK8 R and was told no.
- **Smarter path:** MK7/7.5 R + crashed 8V RS3. A rear-hit 2019 R sold on Copart for US$10,500. A complete dressed DAZA engine was ~US$10k a few years ago. Realistically $25k+ CAD.

---

## 6. Other 07K swap platforms (and the E46)

**Easy (bolt-in kits exist):**
- **MK1 Rabbit/Jetta/Caddy/Scirocco** — S&P Automotive bolt-in 07K mount kit (02J brackets)
- **MK2 / MK3 Golf/Jetta** — Fabless kits ~US$1,745–1,775
- **MK4 Golf/Jetta** — Beetle parts, no kit needed
- **Porsche 944/968 (RWD)** — big community, Boost Brothers base kit ~US$1,250

**E46: no.** No documented 07K E46 swaps; fully custom; and a downgrade (330i ≈ 225 hp vs stock 07K ≈ 170 hp).

**Just-want-300-hp alternatives (rejected — wants the character and the swap):** Infiniti G37 coupe (328 hp, ~$8–9k avg in Ontario); MK7 Golf R (292 hp stock, ~$14–23k in Ontario).

---

## 7. The decision: turbo 07K ZN6

**Goal:** turbo 07K in a ZN6 (FR-S/BRZ/86), ~300 hp, for the character and the build itself, running a custom ECU.

- **ZN6 prices:** FR-S near Toronto ≈ $11.5–21k.
- **Why not K24:** expensive (see §11) and NA power barely beats the FA20.
- **Why a turbo 07K works power-wise:** stock internals reported reliable to ~400 whp (~18 psi) in 944 builds; rods are the weak link; rods/pistons on stock bore have made ~600 whp; a replacement junkyard 07K is ~$300.
- **Longitudinal 07K precedent:** time-attack Miata — notched oil pan, custom exhaust manifold, recessed firewall/modified tunnel, Dodge 8HP via ChathamCNC adapter; first engine died from oil starvation (pan design); ~465 hp / 433 lb-ft.
- **Rough budget:** ~$25k+ CAD all-in including the car (before deciding to make most parts yourself — see §11–12).
- **Prerequisite:** a garage where the car can sit for months.

---

## 8. ECU strategy

### Version 1: stock VW ECU + CAN bridge
- **Engine:** 2005–2008 07K with **ME7.1.1** (MAF). Big DIY tuning scene from the 1.8T world. 2009+ ME17.5 (MAF-less) has fewer turbo options.
- **RevMap swap-ready file:** runs the stock ECU in a non-VW chassis, removes CAN-related codes, immobilizer delete add-on, supports MK4/B6/B7 VW pedals (run a VW pedal, not the ZN6's).
- **Turbo tune:** 034 off-the-shelf for ME7 (8–9 psi stock intake; 15–20 psi with short-runner intake), or DIY.
- **CAN bridge (your build):** microcontroller that reads the VW ECU (RPM, coolant temp, torque) and broadcasts the ZN6 messages the chassis expects — cluster, ABS/VSC, electric power steering, A/C. The proven VW ECU handles safety-critical throttle and knock control. Bridge code later becomes your ECU's CAN module.

### Version 2: your own torque-based ECU
- **Job 1 — run a turbo 07K:** trigger decoding, sequential injection, 5-coil ignition, wideband closed loop, boost control, **knock control**, **drive-by-wire safety** (redundant pedal/TPS plausibility checks, watchdog, limp mode).
- **Job 2 — be a ZN6 ECU on CAN.** Torque-based architecture natively handles VSC torque-reduction requests.
- **Getting the CAN messages:** check FT86Club and comma.ai's opendbc; log the bus yourself → **buy a running ZN6** so you can record the stock ECU's traffic.
- **Fallback reference:** Haltech Elite already has 2013–2016 BRZ/FR-S CAN protocols (used in KPower's K24 kit).

### Test sequence
1. Bench: crank/cam stim + scope to validate decoding and outputs
2. Engine on a run stand — known-good ECU first (stock VW), then yours
3. Log stock ZN6 CAN, build emulation, test on the bus
4. Swap; run NA in the car
5. Turbo last

---

## 9. Transmission

### Stock ZN6 6-speed (TL70, AZ6-derived) — recommended for v1
- 86-community rule of thumb ~350 hp turbo on the stock box; **torque is the limit** — ~300 lb-ft with an upgraded clutch before 3rd/4th tend to break.
- **Cap torque ~280 lb-ft in the tune** → held to 5,600 rpm ≈ 300 hp.
- AZ6 family (Miata, S15, RX-8, Altezza/IS200, 86/BRZ); a countershaft clip mod has pushed it toward ~500 Nm.
- Needs a custom 07K adapter plate, flywheel, clutch — no extra electronics. No off-the-shelf VW-pattern → ZN6 adapter found.

### CD009 (stronger manual)
- **TD Conversions** sells a VW 1.8T/2.0T → Nissan 350Z (CD009/CD00A) adapter kit.
- CD009-in-ZN6 is a known swap (Touge Factory and Collins kits exist for mounts/tunnel).

### ZF 8HP (auto)
- **DomiWorks** VW 1.8T/1.9T → BMW 8HP adapter kit (fits BMW "N57" bellhousing pattern: 8HP45 N47, 8HP50/51 B38/B48/B58, 8HP70/75 N57, 8HP75 B57, 8HP76 S58).
  - Includes: 33 mm anodized aluminum adapter plate, custom billet flywheel (SS2541 high-strength steel), flywheel center guide, bolts and dowels
  - ~15,000 SEK incl. Swedish VAT (switch store to Canada for USD export price); express shipping 3–5 days; expect HST/brokerage on import
  - Not included: torque converter, TCU (they sell TurboLamik / CANTCU), shifter, cooler, driveshaft, mounts; starter location not stated
  - **Ask before buying:** 07K crank flange/center bore fit? Starter location/which starter? Total stack-up length? Recommended converter for ~400 Nm? 07K-specific version (they do custom work and 3D scanning)?
- ChathamCNC made a 07K → Dodge 8HP adapter for the turbo 07K Miata.
- Downsides: needs a TCU on top of the CAN bridge, heavier/bulkier in the ZN6 tunnel, it's an auto.

### Key fact: bellhousing pattern
- The 07K shares the **VW 4-cylinder bellhousing pattern** (1.8T/2.0/TDI). TD Conversions states all VW/Audi 4-cyls share the same bell pattern and crank hub — confirm the 07K's crank hub (6- vs 8-bolt variants exist).
- **Longitudinal Audi 1.8Ts use a different pattern** — make sure any kit is for the VW (transverse) pattern.

### Porsche transmission? No.
944/968 uses a rear transaxle via torque tube (the 944 swap bellhousing bolts the 07K to that torque tube). 911/Boxster/Cayman boxes are rear/mid-engine transaxles. None fit a front-engine ZN6 layout.

### Design difficulty: adapter to 8HP vs to BRZ trans
- **Don't design the 8HP one** — it already exists (DomiWorks).
- **ZN6 adapter is the easier design:** manual stack-up is well understood, no TCU, and the ZN6 bell side is already solved by K-swap kits (KPower K → ZN6 plate is a reference).
- 8HP design would be harder: converter centering, pump engagement depth, flexplate flex.
- **Plan:** design the ZN6 adapter for v1; DomiWorks 8HP kit as the upgrade path.

### Precedent: 07K on an RX-8 AZ6 (Brett Horn's E30 drift car)
*Added Oct 4, 2026. Sources: the descriptions, chapter lists and comment threads of Brett Horn's three videos (his own replies as @brett.mk2), plus the adapter maker's product pages. There are no captions on the videos, so the footage itself hasn't been reviewed. Anything about what's on screen is marked as a viewer comment.*

**Videos:** [RX8 Transmission on a VOLKSWAGEN?](https://www.youtube.com/watch?v=W_twx5oCz6c) (Oct 2024) → [Will The Volkswagen+Mazda Drivetrain Work?](https://youtu.be/QIYwMtbhb1w) (Feb 2025) → [More ISSUES with the 07k Swap](https://www.youtube.com/watch?v=bqJBSB7oPi4) (Dec 2025).

**The adapter: bought, not made.** From **RX8 Gearbox Adapters (UK)** ([rx8gearboxadapters.com](https://www.rx8gearboxadapters.com/)). Brett: *"The company is called 'RX8 Gearbox Adapters'"*. It's their **VW PD / 1.8T 20V → RX-8** plate. The 07K bolts to it because it shares the VW 4-cyl bell pattern (see "Key fact" above).
- **RX8002**, upright/vertical mount: £140. Used in the first video.
- **RX8049**, 20° mount: £155, made to order (~2 weeks). The second video swaps to this "to tilt the engine over at a 20° angle". VW's factory lean is 15°.
- Sold separately: **RX8027** bolt kit, **RX8017** spigot (pilot) bearing.

**What goes between the engine and the gearbox (the maker's recipe):**

| Part | What it is |
|---|---|
| Starter | **Audi A4 5-speed longitudinal PD (TDI) starter**. Brett: "Audi longitudinal 1.8t starter" |
| Flywheel | **Aftermarket single-mass DMF-replacement flywheel** for that Audi longitudinal PD/1.8T application (ring gear on the side the longitudinal starter needs) |
| Pressure plate | Matching Audi/VW pressure plate for that flywheel |
| Clutch disc | **Ford 23-spline friction plate** (fits the RX-8 input shaft). Brett runs a non-stock disc; Southbend Clutch is a sponsor |
| Pilot bearing | RX8017 spigot bearing in the crank |
| Release | Maker says the RX-8 clutch arm, slave and release bearing usually work with little modification (arm pivot height may need adjusting). **Brett couldn't use them** (see below) |

**What went wrong (from his replies and the chapter titles):**
1. **Clearance at the timing cover / vacuum pump.** Chapters: "Overcoming clearance issues", "Modifying the timing cover", "Resolving bolt alignment". The vacuum pump casting on the timing cover is in the way even with the pump deleted. Brett: *"It's the casting on the timing cover that's still in the way."*
2. **The RX-8 external slave and clutch arm don't fit** because of that casting. He went to a **concentric (internal) slave cylinder**, then an **adjustable** one.
3. **Clutch release never worked right in the car.** Video 3: "Adjustable slave cylinder" → "Removing engine for clutch" → "Inspecting clutch components". He had to pull the engine. Viewers point out that release-bearing-to-finger spacing has to be measured properly, and that a bigger (3/4") master cylinder may be needed for throw.
4. **Ring gear warning (viewer comment, unconfirmed):** the flywheel in video 2 looked like a *transverse* one with the ring gear on the clutch side. A longitudinal starter engages from the engine side.
5. Fiddly clutch disc alignment (no RX-8 alignment tool fits the VW crank); pedal box still undecided (probably Wilwood).

**What it means for the ZN6 build:**
- **The engine side is solved and cheap.** Copy the recipe: Audi longitudinal PD starter, a single-mass flywheel for the longitudinal Audi PD/1.8T, the VW pressure plate, and a disc with the **TL70's** input spline in the right diameter. Then only the plate and the stack-up (§13) are custom.
- **The plate itself won't fit.** The RX-8 bell is the 13B pattern, not the TL70's. Two options: ask RX8 Gearbox Adapters to make a VW → ZN6/TL70 version (they already make made-to-order variants), or design ours with their VW side as a reference. They make the plate; a buyer could measure its VW-side bolt circle and dowels from one.
- **Plan clutch actuation early.** Check the 07K timing cover / vacuum pump casting against the ZN6 bell and release fork before choosing the plate thickness. Budget for a concentric slave and measure engagement on the bench before the engine goes in.
- **Possible question:** contact Brett (IG @brett.07k) about final release-bearing spacing, his flywheel part number, and whether the clutch works now.

---

## 10. Turbo and manifold

### Turbo options
- **RS3 / TT RS turbo (best fit):** factory turbo for VW's 2.5 five. **Byiabed** adapter plate (US$449.99) bolts it to the 07K head mimicking the OEM 2.5 TFSI setup (optional OEM support brackets). Turbo + manifold in one; stock K16 ≈ 405 hp on pump on the RS3 engine (a bit less on port-injected 07K). Laid out for transverse — mock up in the ZN6 bay.
- **Golf R IS38: not really.** Built for EA888 (exhaust manifold cast into the head) — would need a custom manifold to its odd flange; no 07K examples found.
- **Reverse-rotation turbo:** mirror-image Garretts (11 models across G-series and GTX Gen II). For ~300 hp on a 2.5, a **G25-550 RR** is a sensible size. GTX30-size RR ≈ US$2,000–2,500. RR turbine housings aren't interchangeable with standard. **Try clocking housings first.**
- **Rear-mount turbo:** avoids engine bay packaging; costs lag, long piping, oil scavenge pump.

### Manifold
- Off-the-shelf 07K manifolds are for transverse VWs. In the ZN6 (flywheel to the rear) the **exhaust faces the passenger side** — less crowded in LHD (steering shaft and brake booster are driver side).
- **Avoid top-mount** — low hood, 07K is taller than the boxer.
- **Build your own:** 3D-scanned 07K header flange model (from a 2009 Beetle) with ports matched to OEM gasket and recesses for 1.68" ID weld els. Print to test fit, laser-cut in steel; SS304 sch10 weld els; bolt flange to a spare head or thick plate while welding to prevent warping.
- Downpipe routing past the crossmember into the tunnel usually decides where the turbo can sit.

### Intake
- RWD 07K intake manifolds are being made in the 07K Facebook community; Boost Brothers also sells a 07K intake manifold.

---

## 11. Cost vs a K24 swap

### K24 (KPower)
- Complete package **from US$10,595**; DIY "Builder" package **US$2,250**; electronics package **US$3,895–4,195**.
- Appears to exclude the K24 itself; result is an NA engine (~200–250 hp).
- KPower's finished K24 BRZ dev car listed at **US$28,900**.

### Turbo 07K DIY (parts, before car)
- Initial estimate: **US$5–9k (≈$7–13k CAD)**
- After "make everything I can" (§12): **US$3.5–7k (≈$5–10k CAD)**

| Item | USD |
|---|---|
| Engine | $300–1,150 |
| Turbo (used RS3 vs new Garrett) | $500–2,000 |
| Raw materials (billet, weld els, sheet, tube) | ~$500–1,000 |
| Clutch | $300–600 |
| Driveshaft shop | $500–900 |
| Fuel system, sensors, fittings | ~$800–1,500 |
| Cooling | ~$400–800 |
| Software | $200–1,000 |

**Where it costs more:** redos (budget +20–30% for adapter/pan/mounts), months of design/fab time, lower resale than a known kit.

---

## 12. Design philosophy: make vs buy

**Rule (yours):** engineer and machine everything you can yourself; buy or outsource parts that are already solved by the community or are safety-critical.

**Make yourself**
- Transmission adapter plate (print a full-scale test plate first; billet 6061/7075 with proper dowels; dial-indicate bore runout)
- Engine/trans mounts (TIG-welded steel, OEM-style rubber isolators)
- Oil pan sump (see §14)
- Turbo manifold, downpipe, intercooler piping, exhaust
- Wiring harness, CAN bridge, ECU
- Brackets, coolant routing, fuel rail adapters

**Buy / outsource**
- **Flywheel** — modify a known-good one or commission it; at minimum professionally balanced
- **Driveshaft** — do the length/critical-speed math, have a shop build and balance it
- Clutch and release bearing; turbo, wastegate, BOV; fuel pump, injectors, sensors, AN fittings; radiator and intercooler core
- 10.9-grade / ARP fasteners wherever it matters

**Biggest unknown:** mill/lathe access (school or Baja shop).

---

## 13. Flywheel, clutch and the bellhousing stack-up

### What's in the bellhousing (engine → trans)

```
 07K block | adapter |  bellhousing (ZN6)                         | ZN6 trans
           |  plate  |                                            |
  crank ===[flange]==[hub][flywheel][disc][pressure plate]  [release brg]
           |   T     |      ^ring gear (starter meshes here)      |
           |         |      ^pilot bearing (input shaft nose)     |
           |<- T ->|<-- X -->|                                    |
         block    bell    friction
         face     face    face
```

- **Power path:** crank → flywheel → clutch disc (clamped by pressure plate's diaphragm spring) → disc splines → input shaft.
- **Release bearing** pushes diaphragm fingers to unclamp.
- **Pilot bearing** supports the input shaft nose.
- **Starter** pinion meshes with the ring gear on the flywheel rim.

### The one dimension that matters: X
**X = distance from the bellhousing mating face to the flywheel friction surface (stock ZN6 value).** If your friction face lands at the stock X, the stock ZN6 clutch, pressure plate, release bearing travel, starter mesh and input shaft engagement all work.

### The equation
Let **c** = position of the 07K crank flange face relative to the block's rear face (may be recessed), **T** = adapter plate thickness.

> **Flywheel offset (crank flange → friction face): D = T + X − c**

The custom flywheel/hub is the part that absorbs the difference between the two layouts.

### What to measure
- **ZN6:** X, input shaft nose protrusion past the bell face (sets pilot depth), ring gear diameter and axial position — on a real gearbox + stock flywheel (junkyard set, or your car before pulling the FA20)
- **07K:** c, crank bolt pattern (6- or 8-bolt), crank center bore/pilot diameter

### Flywheel spec (to commission)
- Offset **D**
- 07K crank bolt pattern
- ZN6 friction diameter + pressure plate bolt pattern (so any off-the-shelf ZN6 clutch kit fits)
- ZN6 ring gear (stock starter works)
- Pilot bearing pocket at the correct depth
- Balanced. Check whether the 07K flywheel carries a balance weight for the five-cylinder — if so, replicate it.

### Flywheel options
1. **Re-drill a stock ZN6 flywheel** to the 07K pattern (watch old FA20 holes), add pilot pocket, correct axial position, dynamically balance — keeps ZN6 clutch/release/starter.
2. **VW 02M flywheel** (bolts to the 07K crank; 944 swaps use it with SPEC clutch packages US$575–825) + hybrid clutch disc with ZN6 input spline + VW starter on the adapter plate — more custom.
3. **Commission a matched adapter + flywheel set** from a custom adapter maker (e.g. Brightstone made-to-order) — they handle stack-up, pilot and balance.

---

## 14. Oil pan

- **Don't build from scratch.**
- **Boost Brothers 944 07K pan — US$1,210:** machined stock upper pan (send your core) + baffled lower sump with trap doors, pickup tube and -10AN turbo oil return. Clears the **944** crossmember with no body mods — **measure against the ZN6 before buying.**
- **If it doesn't fit, copy the method:** modify the cast upper pan to clear the crossmember/steering rack, bolt on a fabricated lower sump; weld in off-the-shelf trap-door baffles.
- **Log oil pressure from day one;** an Accusump is cheap insurance on a track car.
- **Design aid:** SunnyWorks high-res scan of the ZN6 front subframe (Sketchfab). Model crossmember + pan in SolidWorks and print a test sump on the X1C before cutting metal.
- Lesson from the turbo 07K Miata: first engine died of oil starvation from the pan design.

---

## 15. Adapter design and CAD sources

**Plan:** get 3D scans or DXFs of both bolt patterns, design the plate, physically verify.

| Source | What | Notes |
|---|---|---|
| **Bremar Automotion 3D Scan Store** | TL70 (AZ6-derived) 86/BRZ gearbox scan — Base and Premium packs | From a 2016 Australian 86; gearbox minus shifter; **STL mesh, not solid** — rebuild bolt pattern/dowels as sketches |
| **GrabCAD — James Pekarek** | Aisin AZ6 scan | From a 2006 **RX-8** (13B bellhousing — wrong pattern); Einstar ~0.5 mm accuracy — layout only |
| **KPower** | K-series → ZN6 adapter plate (US$579) | Trans side is a precision copy of the ZN6 bell pattern/dowels — great measurement reference |
| **DomiWorks** | Digital parts (some engine/gearbox CAD), 3D scanning, part-to-CAD | Check whether they have yours |
| **SunnyWorks (Sketchfab)** | ZN6 front subframe scan | For oil pan/crossmember clearance |
| **CGTrader** | 07K exhaust header flange model | For manifold building |
| **Your own 07K** | Block rear face | Measure directly; a junk 02J bellhousing is a cheap cross-check |

- No ZN6/TL70 or VW 02J/1.8T bellhousing CAD surfaced on GrabCAD; an FT86Club member was also hunting for BRZ bellhousing CAD in 2025 — clean CAD isn't freely available.
- **Accuracy:** hobby scans (~0.5 mm) aren't good enough for dowel holes. Use scans for layout; verify every critical hole and bore on real parts.
- **AZ6 variants differ by application:** bellhousing bolt pattern/dowels, input shaft nose length (and possibly spline), starter boss, tail housing/shifter/mounts. Only the 86/BRZ TL70 front end is valid for the adapter.
- **Before machining:** print the plate on the X1C and bolt it to both the engine and the gearbox.

### Adapter design checklist
1. **Concentricity:** crank and input shaft axes within ~0.05 mm — dowels on both sides, dial-indicate
2. **Stack-up:** friction face at stock X (see §13)
3. **Pilot bearing** pocket (flywheel or crank adapter)
4. **Crank flange:** confirm 6- vs 8-bolt 07K
5. **Plate thickness** vs ZN6 bay packaging (thick plates push the engine forward)

---

## 16. Open items

- Get the Bremar TL70 scan; measure X, pilot depth and ring gear position on a real ZN6 box + flywheel
- Confirm the 07K crank flange (6/8-bolt, center bore) and measure c
- Decide v1 transmission: stock ZN6 6-speed (custom adapter) vs CD009 (TD Conversions kit) — 8HP (DomiWorks) as upgrade path
- If considering 8HP: send DomiWorks the five questions in §9
- Model the ZN6 bay in SolidWorks: engine, adapter, turbo/downpipe routing, oil pan vs subframe
- Buy a **running** ZN6 so the stock CAN traffic can be logged
- Secure garage space and machine shop access
- Ask RX8 Gearbox Adapters (UK) whether they'd make a VW PD/1.8T → ZN6/TL70 plate; otherwise use their VW side as the reference
- Confirm the TL70 clutch disc spline/diameter so a disc can be matched to the Audi PD single-mass flywheel + VW pressure plate
- Check the 07K timing cover/vacuum pump casting against the ZN6 release fork and slave location (Brett had to go to a concentric slave)

---

## 17. Sources

**MK4 swap**
- [RevMap Performance — 07K swap-ready file](https://revmapperformance.com/product/07k-swap-ready-file/)
- [RevMap — "Charles" pinout tool](https://charles.revmapperformance.com/)
- [Fabless Manufacturing — MK3 07K swap kit](https://fablessmanufacturing.com/engine-swap-kit-vw-mk3-2-5l-07k/)
- [Fabless Manufacturing — MK2 07K swap kit](https://fablessmanufacturing.com/engine-swap-kit-vw-mk2-2-5l-07k/)
- [eBay — 2.5L 07K with ECU wiring](https://www.ebay.com/itm/355614546913)
- [Kijiji — MK4 Jetta listings, Ontario](https://www.kijiji.ca/b-cars-trucks/ontario/mk4-volkswagen-jetta/k0c174l9004)

**Importing**
- [RIV — FAQ](https://www.riv.ca/helpfaqs.aspx)
- [Beacon Hill — Importing a vehicle from the US (2026)](https://beaconhillwm.ca/how-to-import-your-vehicle-to-canada-from-the-u-s/)
- [GST/HST rules for importing used vehicles](https://lawyerinfo.ca/guides/money-taxes-ip/gst-hst-rules-for-importing-used-vehicles-into-canada-from-the-us/)
- [LCS Logistics — Import costs](https://lcslogistics.com/how-much-does-it-cost-to-import-a-car-from-us-to-canada/)
- [USD/CAD rate](https://usd.currencyrate.today/cad)

**AWD**
- [TDIClub — Golf 4 4Motion conversion](https://forums.tdiclub.com/showthread.php?t=276145)
- [TDIClub — What is needed for AWD conversion](https://forums.tdiclub.com/showthread.php?t=343391)
- [GolfMKV — AWD conversion / VW bolt pattern](http://www.golfmkv.com/forums/showthread.php?t=136710)
- [JustAnswer — MK4 R32 swap](https://www.justanswer.com/vw-volkswagen/tw0ef-2002-front-wheel-drive-engine-conversion-kit.html)

**Golf R / RS3**
- [IAA — Golf R salvage listings](https://www.iaai.com/Vehiclelisting/Volkswagen/Golf%20R)
- [Motor1 — Golf R with RS3 inline-five](https://www.motor1.com/news/580667/vw-golf-r-inline-five/)
- [Engine Swap Depot — Innovative Motorsports build](https://engineswapdepot.com/?p=91851)
- [VWVortex — Golf 7R 2.5 TFSI build](https://www.vwvortex.com/threads/golf-7r-2-5-tfsi-build.9404821/)
- [Copart/IAAI sale history](https://autohelperbot.com/en/sales)

**Other platforms / alternatives**
- [S&P Automotive — MK1 07K bundle](https://s-pautomotive.com/product/mk1-07k-bolt-in-conversion-bundle/)
- [CarGurus — G37 in Ontario](https://www.cargurus.ca/Cars/l-Used-INFINITI-G37-Ontario-d1036_L412505)
- [CarGurus — Golf R near Ottawa](https://www.cargurus.ca/Cars/l-Used-Volkswagen-Golf-R-Ottawa-d2131_L412564)
- [Kijiji — Golf R in Ontario](https://www.kijiji.ca/b-cars-trucks/ontario/volkswagen-golf-r/k0c174l9004)

**ZN6 / K24**
- [CarGurus — FR-S near Toronto](https://www.cargurus.ca/Cars/l-Used-Scion-FR-S-Toronto-d2140_L414276)
- [FT86Club — K24 swap CAN thread](https://www.ft86club.com/forums/showthread.php?t=125252)
- [KPower — 86 conversion](https://kpower.industries/blogs/news/the-kpower-86-swap-is-here)
- [KPower — Complete K swap package](https://kpower.industries/products/complete-kpower-86-conversion-package)
- [KPower — Builder package](https://kpower.industries/products/kpower-86-builder-kit)
- [KPower — Link electronics package](https://kpower.industries/products/kpower-86-link-electronics-package)
- [KPower — 86 swap components](https://kpower.industries/collections/kpower-86-swap)
- [Engine Swap Depot — KPower BRZ for sale](https://engineswapdepot.com/?p=144051)
- [Collins — K-series to FRS/BRZ kit](https://collinsperformancetechnologies.com/products/k-series-to-frs-brz-ft86-swap-kit)
- [Wiring Specialties — FRS/BRZ K-swap harness](https://www.wiringspecialties.com/honda-k-series-haltech-elite-ecu-wiring-harness-for-rwd-frs-brz-gt86-canbus-pro-series/)

**Turbo 07K / longitudinal**
- [Rennlist — 07K swap thread (944)](https://rennlist.com/forums/944-turbo-and-turbo-s-forum/803341-vw-audi-07k-2-5l-20v-i5-swap-thread.html)
- [Rennlist — 07K power on stock internals](https://rennlist.com/forums/944-turbo-and-turbo-s-forum/803341-vw-audi-07k-2-5l-20v-i5-swap-thread-164.html)
- [Rennlist — RS3 turbo sizing on 07K](https://rennlist.com/forums/944-turbo-and-turbo-s-forum/803341-vw-audi-07k-2-5l-20v-i5-swap-thread-71.html)
- [VWVortex — 2.5L turbo build resource](https://www.vwvortex.com/threads/2-5l-turbo-build-your-own-kit-resource-2020.9427505/)
- [VWVortex — 034 07K tunes](https://www.vwvortex.com/aftermarket-and-industry-news/volkswagen-jettarabbit-2-5l-tuning-now-available-034-motorsport/)
- [Engine Swap Depot — Turbo 07K Miata](https://engineswapdepot.com/?p=147945)
- [Miata.net — RWD 07K intake manifolds](https://forum.miata.net/vb/showthread.php?t=779263)
- [Byiabed — 07K to TT-RS turbo adapter](https://byiabed.com/07K-25-Rabbit-to-TT-RS-Turbocharger-adapter-plate_p_143.html)
- [VWVortex — IS38 turbo upgrade](https://www.vwvortex.com/threads/is38-turbo-upgrade.8371177/)
- [Garrett — Reverse rotation turbochargers](https://www.garrettmotion.com/news/newsroom/article/reverse-rotation-turbochargers-a-unique-performance-configuration-for-single-and-twin-turbo-applications/)
- [AMS — Garrett reverse rotation](https://www.amsperformance.com/blog/2016/11/01/garrett-reverse-rotation-turbochargers/)
- [Garrett — Performance turbo lineup](https://www.garrettmotion.com/racing-and-performance/performance-turbos/)
- [AMS — GTX turbo assembly kits](https://www.amsperformance.com/product-category/ams-turbo/turbochargers/garrett-gtx-series/garrett-gtx-turbo-assembly-kits/)
- [CGTrader — 07K header flange model](https://www.cgtrader.com/3d-print-models/hobby-diy/automotive/vw-07k-exhaust-header-flange-3d-model)
- [EngineBasics — Building a turbo manifold](https://www.enginebasics.com/Advanced%20Engine%20Tuning/Turbo%20manifold%20How%20to.html)

**Transmission**
- [FT86Club — Stock FR-S transmission limits](https://www.ft86club.com/forums/showthread.php?p=3262459)
- [MiataTurbo — AZ6 countershaft mod / applications](https://www.miataturbo.net/suspension-brakes-drivetrain-49/500nm-torque-nb-6-speed-transmission-105065/)
- [TD Conversions — VW adapter kits](https://tdconversions.com/collections/volkswagen-kits)
- [TD Conversions — VW crank hub / bell pattern note](https://tdconversions.com/products/vw-1-9-2-0l-tdi-to-ford-4-0l-adapter-kit-automatic)
- [Touge Factory — FRS/BRZ swap kits](https://www.tf-works.com/frs-brz-1/)
- [DomiWorks — VW 1.8T to BMW 8HP adapter kit](https://www.domi-works.com/products/vw-1-8t-1-8t-to-bmw-8hp-45-50-70-75-n47-n57-b57-b58-s58-adapter-kit)
- [Autosports Engineering — 8HP conversions](https://www.autosportsengineering.com/products/ls-lt-dodge-mopar-8hp-conversion-kit-8hp70-75-90-95-ase)
- [Classic Motorsports — VW vs Audi bell patterns](https://classicmotorsports.com/forum/grm/rwd-trans-that-bolts-to-a-2003-18t-jetta-motor/124541/page1/)
- [Brett Horn — MAZDA RX8 Transmission on a VOLKSWAGEN? (E30 07K build)](https://www.youtube.com/watch?v=W_twx5oCz6c)
- [Brett Horn — Will The Volkswagen+Mazda Drivetrain for the BMW E30 Drift Car Work?](https://youtu.be/QIYwMtbhb1w)
- [Brett Horn — More ISSUES with the 07k Swap BMW E30 Drift Car](https://www.youtube.com/watch?v=bqJBSB7oPi4)
- [PMC Motorsport — RX-7/RX-8 gearbox adapter plates](https://pmcmotorsport-shop.com/eng_m_Transmission_Gearbox-Adapter-Plates_Mazda-RX-7-RX-8-Gearbox-Adapter-Plates-509.html)
- [Collins — K-series to RX-8 adapter plate + flywheel](https://collinsperformancetechnologies.com/products/honda-k-series-to-mazda-rx-8-adapter-plate-flywheel-partial-swap-kit)
- [RX8 Gearbox Adapters — VW PD/1.8T 20V vertical (RX8002)](https://www.rx8gearboxadapters.com/product-page/vw-pd-1-8t-20v-vertically-mounted)
- [RX8 Gearbox Adapters — VW PD/1.8T 20V 20° (RX8049)](https://www.rx8gearboxadapters.com/product-page/copy-of-vw-pd-1-8t-20v-mounted-20degrees)
- [R3VLimited — M20 to RX-8 6-speed adaptor plates](https://www.r3vlimited.com/board/forum/e30-technical-forums/general-technical/9868970-m20-rx8-6-speed-adaptor-plates)
- [Brightstone — Custom adapter plates](https://brightstoneengineering.com/products/custom-gearbox-adapter-plates-precision-cnc-machined-in-the-uk)

**Oil pan / CAD**
- [Boost Brothers — 944 07K oil pan](https://www.boostbrothersgarage.com/products/944-07k-swap-oil-pan)
- [Boost Brothers — 944 07K swap parts](https://www.boostbrothersgarage.com/collections/944-07k-swap)
- [Sketchfab — 86/FRS/BRZ front subframe scan](https://sketchfab.com/3d-models/86-frs-brz-front-subframe-model-96c9112eee00459089a809713f6b00d2)
- [Bremar — TL70 AZ6 gearbox scan (Base)](https://www.bremar3dscanstore.com/all-scan-files/p/tl70-az6-gearbox)
- [Bremar — TL70 AZ6 gearbox scan (Premium)](https://www.bremar3dscanstore.com/all-scan-files/p/tl70-az6-gearbox-premium)
- [GrabCAD — James Pekarek's AZ6 (RX-8) scan](https://grabcad.com/james.pekarek-1/models)
- [FT86Club — Bellhousing CAD drawings thread](https://www.ft86club.com/forums//showthread.php?p=3616525)
