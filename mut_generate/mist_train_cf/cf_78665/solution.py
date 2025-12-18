"""
QUESTION:
Define two functions in Python, `g(x)` and `dg(x)`, representing a trigonometric polynomial and its derivative, respectively. `g(x)` should be defined as `4 * sin^2(x) + 7 * cos(x) + 1`, and `dg(x)` as its derivative `8 * sin(x) * cos(x) - 7 * sin(x)`. The functions should use the NumPy library for the trigonometric operations. Calculate `g(π/3)`, `dg(π/3)`, and forecast `g(π/2)` using the Taylor Series expansion with `h = π/2 - π/3`.
"""

import numpy as np

def entrance(x):
    g_value = 4 * np.sin(x)**2 + 7 * np.cos(x) + 1
    dg_value = 8 * np.sin(x) * np.cos(x) - 7 * np.sin(x)
    return g_value, dg_value