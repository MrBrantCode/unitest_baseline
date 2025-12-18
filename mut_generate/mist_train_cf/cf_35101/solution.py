"""
QUESTION:
Implement a function `runge_kutta(f, t0, u0, t_end, h)` that uses the fourth-order Runge-Kutta method to approximate the solution of a system of first-order ordinary differential equations (ODEs) defined by the function `f(t, u)`, where `f` returns an array of derivatives with respect to `t`, `t0` is the initial time, `u0` is the initial condition, `t_end` is the end time, and `h` is the time step. The function should return two arrays: the time points `t` and the corresponding solution values `u`.
"""

def runge_kutta(f, t0, u0, t_end, h):
    t = [t0]
    u = [u0]
    while t[-1] < t_end:
        k1 = h * f(t[-1], u[-1])
        k2 = h * f(t[-1] + 0.5*h, u[-1] + 0.5*k1)
        k3 = h * f(t[-1] + 0.5*h, u[-1] + 0.5*k2)
        k4 = h * f(t[-1] + h, u[-1] + k3)
        u_new = u[-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        t.append(t[-1] + h)
        u.append(u_new)
    return np.array(t), np.array(u)