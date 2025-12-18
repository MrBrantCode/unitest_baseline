"""
QUESTION:
Write a Python function named `likelihood_contribution` that calculates the likelihood contribution from a sample of survival time `x` with right-truncation time `Y_R` and probability density function `f` and survival function `S`. The function should take `x`, `Y_R`, `f`, and `S` as input and return the likelihood contribution. The input `f` and `S` are functions.
"""

def likelihood_contribution(x, Y_R, f, S):
    """
    Calculate the likelihood contribution from a sample of survival time x 
    with right-truncation time Y_R and probability density function f and survival function S.

    Parameters:
    x (float): Survival time
    Y_R (float): Right-truncation time
    f (function): Probability density function
    S (function): Survival function

    Returns:
    float: Likelihood contribution
    """
    return f(x) / (1 - S(Y_R))