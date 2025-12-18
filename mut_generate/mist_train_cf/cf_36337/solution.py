"""
QUESTION:
Implement a function `double_integral` that calculates the double integral of a 2D array using the trapezoidal rule. The function should take in a 2D array of values `Zs`, a 1D array of x coordinates `ech_x`, and a 1D array of y coordinates `ech_y`, and return the result of the double integral. The function should handle the input arrays properly and return the accurate result of the double integral. The function should be able to handle arrays of any size, and it should not assume any specific distribution of the input values.
"""

import numpy as np

def double_integral(Zs, ech_x, ech_y):
    """
    Calculate the double integral of a 2D array using the trapezoidal rule.

    Args:
    Zs (ndarray): 2D array of values to be integrated
    ech_x (ndarray): 1D array of x coordinates
    ech_y (ndarray): 1D array of y coordinates

    Returns:
    float: Result of the double integral
    """
    int_x = np.trapz(Zs, axis=-1, x=ech_x)
    int_xy = np.trapz(int_x, axis=-1, x=ech_y)
    return int_xy