# Lorentz force simulation

`lorentz_simulation.py` integrates the equation of motion for a charged particle
in uniform electric and magnetic fields and animates the trajectory in 3D.

## Features

- RK45 integration with `scipy.integrate.solve_ivp`.
- Sliders for charge, mass, and all components of **E** and **B**.
- Presets for circular cyclotron motion, a helix, linear acceleration, and
  **E × B** drift.
- Automatic axis limits that follow the trajectory.

## Run

```bash
pip install numpy scipy matplotlib
python lorentz_simulation.py
```
