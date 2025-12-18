"""
QUESTION:
Estimate the Maximum Likelihood of the polynomial logistic regression model with a binomial distribution, given by the equation Na=N (exp(p0 + p1 N + p2 N^2 + p3 N^3 )) / (1 + exp(p0 + p1 N + p2 N^2 + p3 N^3)), where p0, p1, p2, and p3 are the constant, linear, quadratic, and cubic coefficients to be estimated, respectively. The parameters should be estimated using a numerical method such as Newton-Raphson or gradient ascent.
"""

def estimate_maximum_likelihood(N, Na, p0, p1, p2, p3):
    """
    Estimates the Maximum Likelihood of the polynomial logistic regression model.

    Parameters:
    N (array-like): The observed values.
    Na (array-like): The observed response.
    p0, p1, p2, p3 (floats): The constant, linear, quadratic, and cubic coefficients.

    Returns:
    float: The Maximum Likelihood.
    """
    import numpy as np
    
    # Define the polynomial logistic regression function
    def f(N, p0, p1, p2, p3):
        return N * np.exp(p0 + p1 * N + p2 * N**2 + p3 * N**3) / (1 + np.exp(p0 + p1 * N + p2 * N**2 + p3 * N**3))
    
    # Calculate the log-likelihood
    log_likelihood = np.sum(Na * np.log(f(N, p0, p1, p2, p3)) + (N - Na) * np.log(1 - f(N, p0, p1, p2, p3)))
    
    return log_likelihood