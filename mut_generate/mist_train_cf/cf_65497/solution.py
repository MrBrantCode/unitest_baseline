"""
QUESTION:
Create a function `hessian_matrix` to calculate the Hessian matrix of the given scalar-valued function `f(x, y, z) = x^4 + y^4 + z^4`. The function should take the input variables `x`, `y`, and `z` as arguments and return the Hessian matrix `H` as a 3x3 matrix.
"""

import numpy as np

def hessian_matrix(x, y, z):
    """
    Calculate the Hessian matrix of the function f(x, y, z) = x^4 + y^4 + z^4.
    
    Parameters:
    x (float): The x-coordinate of the point.
    y (float): The y-coordinate of the point.
    z (float): The z-coordinate of the point.
    
    Returns:
    H (numpy array): The 3x3 Hessian matrix.
    """
    
    # Calculate the second order partial derivatives
    f_xx = 12*x**2
    f_xy = 0
    f_xz = 0
    f_yx = 0
    f_yy = 12*y**2
    f_yz = 0
    f_zx = 0
    f_zy = 0
    f_zz = 12*z**2
    
    # Create the Hessian matrix
    H = np.array([[f_xx, f_xy, f_xz],
                  [f_yx, f_yy, f_yz],
                  [f_zx, f_zy, f_zz]])
    
    return H