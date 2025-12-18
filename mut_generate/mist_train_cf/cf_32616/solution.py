"""
QUESTION:
Implement the function `make_num_jacobians` to generate Jacobian matrices using the complex-step differentiation (CSD) method. The function should create the matrices `h_y_mat` and `h_p_mat` based on the dimensions of the system, which are provided by `n_y` for the number of equations with respect to the dependent variables and `n_p_d` for the number of parameters. The function uses a fixed step size `h` of 1e-100 and returns the generated matrices. The `make_num_jacobians` function has access to the variables `num_deriv_type`, `n_y`, and `n_p_d`.
"""

import numpy as np

def make_num_jacobians(num_deriv_type, n_y, n_p_d):
    """
    Generate Jacobian matrices using the complex-step differentiation (CSD) method.

    Parameters:
    num_deriv_type (str): Numerical differentiation type, should be 'csd'.
    n_y (int): Number of equations with respect to the dependent variables.
    n_p_d (int): Number of parameters.

    Returns:
    h_y_mat (numpy.ndarray): Jacobian matrix for the dependent variables.
    h_p_mat (numpy.ndarray): Jacobian matrix for the parameters.
    """
    if num_deriv_type == 'csd':
        h = 1e-100
        h_y_mat = h * np.eye(n_y, n_y)
        h_p_mat = h * np.eye(n_p_d, n_p_d)
        return h_y_mat, h_p_mat