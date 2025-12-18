"""
QUESTION:
Implement a function `inverse_normalization(x_res, u_res, s_res, Um, Ul, Ut)` that takes the following inputs:
- `x_res`: A 2D numpy array representing the normalized state variables with shape (n, m), where n is the number of state variables and m is the number of data points.
- `u_res`: A 1D numpy array representing the normalized control variables with shape (m,).
- `s_res`: A scalar representing the normalized scaling factor.
- `Um`, `Ul`, `Ut`: Known scaling factors.

The function should return the following outputs:
- `x_orig`: A 2D numpy array representing the original unscaled state variables with shape (n, m).
- `u_orig`: A 1D numpy array representing the original unscaled control variables with shape (m,).
- `tf`: A scalar representing the original unscaled scaling factor.

Note that the function should reverse the effects of a normalization process that was performed using the scaling factors `Um`, `Ul`, and `Ut`.
"""

import numpy as np

def inverse_normalization(x_res, u_res, s_res, Um, Ul, Ut):
    x_orig = np.copy(x_res)  
    u_orig = np.copy(u_res)  
    tf = s_res * Ut  

    x_orig[0, :] /= Um
    x_orig[1:4, :] /= Ul
    x_orig[4:7, :] /= Ul / Ut
    x_orig[11:14, 0] /= 1. / Ut

    u_orig /= Um * Ul / Ut**2

    return x_orig, u_orig, tf