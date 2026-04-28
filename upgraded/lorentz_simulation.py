import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

def lorentz_deriv(t, state, q, m, E, B):
    """Calculates the derivative of the state vector for a charged particle."""
    v = state[3:]
    a = (q / m) * (E + np.cross(v, B))
    return np.concatenate([v, a])

def run_simulation(q, m, E, B, y0, t_span=(0, 20), num_points=400):
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    sol = solve_ivp(lorentz_deriv, t_span, y0, args=(q, m, E, B), t_eval=t_eval, method='RK45')
    return sol.t, sol.y

def main():
    # Initial Parameters
    q_init, m_init = 1.0, 1.0
    E_init, B_init = np.array([0.0, 0.0, 0.1]), np.array([0.0, 0.0, 1.0])
    y0 = [0.0, 1.0, 0.0, 1.0, 0.0, 0.0]

    fig = plt.figure(figsize=(16, 10))
    plt.suptitle("Code of Zain Ul Abideen\nUpgraded by Claude Code + Gemma4", fontsize=14)
    ax = fig.add_axes([0.3, 0.1, 0.65, 0.8], projection='3d')

    t, coords = run_simulation(q_init, m_init, E_init, B_init, y0)
    line, = ax.plot([], [], [], color='blue', lw=2, label='Trajectory')
    point, = ax.plot([], [], [], 'ro', markersize=5, label='Particle')

    def setup_axes(c):
        for i in range(3):
            mi, ma = np.min(c[i]), np.max(c[i])
            if ma == mi: mi, ma = mi - 1, ma + 1
            ax.set_xlim(mi, ma) if i == 0 else None
            ax.set_ylim(mi, ma) if i == 1 else None
            ax.set_zlim(mi, ma) if i == 2 else None
        ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
        ax.legend()

    setup_axes(coords)

    # Sliders
    sliders = {}
    configs = [
        ('q', 'Charge (q)', 0.1, 5.0, q_init), ('m', 'Mass (m)', 0.1, 5.0, m_init),
        ('ex', 'E_x', -2.0, 2.0, E_init[0]), ('ey', 'E_y', -2.0, 2.0, E_init[1]),
        ('ez', 'E_z', -2.0, 2.0, E_init[2]), ('bx', 'B_x', -5.0, 5.0, B_init[0]),
        ('by', 'B_y', -5.0, 5.0, B_init[1]), ('bz', 'B_z', -5.0, 5.0, B_init[2]),
    ]
    for i, (name, label, low, high, init) in enumerate(configs):
        sliders[name] = Slider(plt.axes([0.12, 0.7 - i*0.06, 0.18, 0.03]), label, low, high, valinit=init)

    def update_simulation(val=None):
        nonlocal t, coords
        E = np.array([sliders['ex'].val, sliders['ey'].val, sliders['ez'].val])
        B = np.array([sliders['bx'].val, sliders['by'].val, sliders['bz'].val])
        t, coords = run_simulation(sliders['q'].val, sliders['m'].val, E, B, y0)
        setup_axes(coords)
        fig.canvas.draw_idle()

    for s in sliders.values(): s.on_changed(update_simulation)

    # Presets
    presets = {
        'Circle': {'q': 1.0, 'm': 1.0, 'ex': 0.0, 'ey': 0.0, 'ez': 0.0, 'bx': 0.0, 'by': 0.0, 'bz': 1.0},
        'Helix': {'q': 1.0, 'm': 1.0, 'ex': 0.0, 'ey': 0.0, 'ez': 0.1, 'bx': 0.0, 'by': 0.0, 'bz': 1.0},
        'Linear': {'q': 1.0, 'm': 1.0, 'ex': 0.5, 'ey': 0.0, 'ez': 0.0, 'bx': 0.0, 'by': 0.0, 'bz': 0.0},
        'Drift': {'q': 1.0, 'm': 1.0, 'ex': 0.2, 'ey': 0.0, 'ez': 0.0, 'bx': 0.0, 'by': 0.0, 'bz': 1.0}
    }

    btn_objs = []
    for i, (name, p) in enumerate(presets.items()):
        btn = Button(plt.axes([0.05 + i*0.11, 0.05, 0.08, 0.05]), name)
        btn.on_clicked(lambda event, params=p: [sliders[k].set_val(v) for k, v in params.items()] or update_simulation())
        btn_objs.append(btn)

    def init():
        line.set_data([], []); line.set_3d_properties([])
        point.set_data([], []); point.set_3d_properties([])
        return line, point

    def animate(frame):
        line.set_data(coords[0, :frame], coords[1, :frame]); line.set_3d_properties(coords[2, :frame])
        point.set_data([coords[0, frame]], [coords[1, frame]]); point.set_3d_properties([coords[2, frame]])
        return line, point

    ani = FuncAnimation(fig, animate, frames=len(t), init_func=init, interval=20, blit=False)
    plt.show()

if __name__ == "__main__":
    main()
