"""
QUESTION:
Given the definitions of frontier portfolios p and q with returns R_p and R_q, and weights x_p and x_q, prove the equation for the covariance between the two portfolios: cov(x_p, x_q) = x_p Ω x_q = C/D * [E(R_p) - A/C] * [E(R_q) - A/C] + 1/C, where Ω is the covariance matrix for the asset returns, C and D are constants, A is the expected return on the minimum variance portfolio, and E(R_p) and E(R_q) are the expected returns of the portfolios.
"""

import numpy as np

def calculate_covariance(R_p, R_q, C, D, A, Omega):
    """
    Calculate the covariance between two frontier portfolios p and q.

    Parameters:
    R_p (float): Expected return of portfolio p
    R_q (float): Expected return of portfolio q
    C (float): Constant depending on the investment universe
    D (float): Constant depending on the investment universe
    A (float): Expected return on the minimum variance portfolio
    Omega (numpy array): Covariance matrix for the asset returns

    Returns:
    float: Covariance between portfolios p and q
    """
    # Calculate the coefficients a_p and b_p
    a_p = R_p - A
    b_p = 1
    
    # Calculate the coefficients a_q and b_q
    a_q = R_q - A
    b_q = 1
    
    # Calculate the covariance
    cov = (C/D) * ((a_p + b_p * A) - A/C) * ((a_q + b_q * A) - A/C) + 1/C
    
    return cov