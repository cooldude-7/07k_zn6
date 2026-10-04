# Intake manifold CAD (CadQuery)

`intake_manifold.py` generates the 07K RWD short-runner intake as STEP solids into `out/`.
Inputs (from SolidWorks, STEP AP214) are in `inputs/`. Re-run with `python3 cad/intake_manifold.py`
after editing the parameters at the top of the script (needs `pip install cadquery`).

Orientation: X along the engine (cylinder 1 assumed at the X=0 end of the flange file), Y outboard
from the head face, Z up (tabbed flange edge with the centre lug = top). Throttle body on the front end.

Outputs: `00_assembly.step` (all bodies), `00_merged_for_flowsim.step` (one solid for SolidWorks Flow
Simulation), individual part STEPs, `preview.png`.
