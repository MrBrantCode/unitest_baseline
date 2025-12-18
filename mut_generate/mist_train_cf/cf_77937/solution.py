"""
QUESTION:
Express the function beta(gamma) where beta = cov(log(W+X),log(Y)) / var(log(W+X)) and gamma = cov(log(W),log(Y)) / var(log(W)), given that W, X, and Y are all random variables. Do not use any additional information other than the given equations for beta and gamma.
"""

import numpy as np

def beta(W, X, Y):
    """
    Calculate beta = cov(log(W+X),log(Y)) / var(log(W+X))
    
    Parameters:
    W (numpy array): A random variable
    X (numpy array): A random variable
    Y (numpy array): A random variable
    
    Returns:
    float: The calculated beta value
    """
    log_W_X = np.log(W + X)
    log_Y = np.log(Y)
    
    cov_log_W_X_log_Y = np.cov(log_W_X, log_Y)[0, 1]
    var_log_W_X = np.var(log_W_X)
    
    return cov_log_W_X_log_Y / var_log_W_X