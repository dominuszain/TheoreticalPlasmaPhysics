# Lorentz Force Trajectory Simulation

A modernized Python implementation of a charged particle trajectory simulation in electric ($\mathbf{E}$) and magnetic ($\mathbf{B}$) fields, originally developed by Zain Ul Abideen and upgraded by Claude Code + Gemma4.

## Features
- **Numerical Integration**: Uses `scipy.integrate.solve_ivp` with the RK45 method to solve the Lorentz force equation: $\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$.
- **Interactive 3D Visualization**: Real-time 3D animation using `matplotlib` that displays the particle's path with a "comet" effect (trailing line and moving head).
- **Dynamic Parameter Control**: 
    - **Sliders**: Adjust charge ($q$), mass ($m$), and all components of the electric ($\mathbf{E}$) and magnetic ($\mathbf{B}$) fields on the fly.
    - **Presets**: One-click buttons to generate common plasma physics trajectories:
        - **Circle**: Pure cyclotron motion.
        - **Helix**: Helical motion along a magnetic field.
        - **Linear**: Constant acceleration in an electric field.
        - **Drift**: $\mathbf{E} \times \mathbf{B}$ drift motion.
- **Auto-Scaling**: The 3D display window automatically adjusts its boundaries to fit the particle's trajectory regardless of the parameter settings.

## Installation

Ensure you have Python 3.x installed along with the following dependencies:

```bash
pip install numpy scipy matplotlib
```

## Usage

Run the simulation using the following command:

```bash
python3 lorentz_simulation.py
```

## How it Works
The simulation defines the state vector as $\mathbf{S} = [x, y, z, v_x, v_y, v_z]$. The derivative function calculates the acceleration $\mathbf{a} = \frac{q}{m}(\mathbf{E} + \mathbf{v} \times \mathbf{B})$, which is then integrated over time to produce the 3D trajectory.

## Credits
- Original Code: Zain Ul Abideen
- Modernization: Claude Code + Gemma4
