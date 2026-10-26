# Lorentz force trajectories

**Charged-particle motion in electric and magnetic fields**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scilab](https://img.shields.io/badge/Scilab-6.x-D35400)](https://www.scilab.org/)

This project integrates the Lorentz force for a charged particle in uniform
electric and magnetic fields. The original Scilab code uses `ode` on a
six-component state vector. The Python version uses `solve_ivp` and adds a 3D
animation with live controls for the fields and particle parameters.

**Author:** Zain Ul Abideen
**GitHub repository:** [dominuszain/TheoreticalPlasmaPhysics](https://github.com/dominuszain/TheoreticalPlasmaPhysics)

## Results

| | |
|---|---|
| ![Trajectory 1](docs/figures/1.png) | ![Trajectory 2](docs/figures/2.png) |
| ![Trajectory 3](docs/figures/3.png) | ![Trajectory 4](docs/figures/4.png) |
| ![Trajectory 5](docs/figures/5.png) | ![Trajectory 6](docs/figures/6.png) |

## Python simulation

```bash
cd python
pip install numpy scipy matplotlib
python lorentz_simulation.py
```

Use the sliders to change `q`, `m`, `E`, and `B`. The preset buttons reproduce
cyclotron motion, a helix, linear acceleration, and **E × B** drift. See
[`python/README.md`](python/README.md).

## Original Scilab code

Open `main.sce` in Scilab and run it. The state vector is
`[x, y, z, vx, vy, vz]`, and the script integrates

```
dv/dt = (q/m) (E + v × B)
```

with Scilab's `ode`. The course report is [`main.pdf`](main.pdf).

## Repository layout

```
.
├── python/           # interactive Python simulation
├── docs/figures/     # example trajectories
├── main.sce          # original Scilab code
├── main.pdf          # course report
├── CITATION.cff
└── LICENSE
```

## Citation

```bibtex
@software{ulabideen_lorentz_2026,
  author = {Ul Abideen, Zain},
  title  = {Lorentz force trajectories},
  year   = {2026},
  url    = {https://github.com/dominuszain/TheoreticalPlasmaPhysics}
}
```

## License

Released under the [MIT License](LICENSE).
