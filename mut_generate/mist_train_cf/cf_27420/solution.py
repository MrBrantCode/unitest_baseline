"""
QUESTION:
Implement the function `runge_kutta_4th_order` that takes the step size `h`, the current values of the independent variable `x`, the dependent variable `y`, and its derivative `u` as input. The function should return the new values of `y` and `u` after applying the fourth-order Runge-Kutta method to the differential equations `dy/dx = u` and `du/dx = -y`.
"""

def runge_kutta_4th_order(h, x, y, u):
    K1 = h * u
    L1 = h * (-y)
    K2 = h * (u + L1/2)
    L2 = h * (-(y + K1/2))
    K3 = h * (u + L2/2)
    L3 = h * (-(y + K2/2))
    K4 = h * (u + L3)
    L4 = h * (-(y + K3))

    y_new = y + (K1 + 2*K2 + 2*K3 + K4)/6
    u_new = u + (L1 + 2*L2 + 2*L3 + L4)/6

    return y_new, u_new