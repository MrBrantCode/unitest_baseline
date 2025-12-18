"""
QUESTION:
Implement a function `kloeden_4_20(a=1)` that returns an object encapsulating the drift, diffusion, and explicit solution functions for the stochastic differential equation (SDE) `dX_t = -0.5*a^2 X_t dt - a*sqrt(1 - (X_t)^2) dW_t`. The drift function is `-0.5*a^2*x`, the diffusion function is `-a*sqrt(1 - x^2)`, and the explicit solution function is `cos(a*W_t + arccos(x_0))`, where `x_0` is the initial value of the stochastic process, `t` is the time, and `W_t` is the Wiener process at time `t`.
"""

import numpy as np

def kloeden_4_20(a=1):
    """Returns a function implementing the explicit solution to the SDE
                dX_t = -0.5*a^2 X_t dt - a*sqrt(1 - (X_t)^2) dW_t
    Taken from (Kloden & Platen, 1992), page 121.
    """
    drift = lambda x, t : -0.5*a*a*x
    diffusion = lambda x, t : -a*np.sqrt(1 - x**2)
    true_sol = lambda x0, t, wt : np.cos(a*wt + np.arccos(x0))
    return drift, diffusion, true_sol