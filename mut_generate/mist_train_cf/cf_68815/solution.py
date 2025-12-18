"""
QUESTION:
Given a multivariate normal distribution $(X_1, ..., X_n)^T \sim \mathcal{N}(\mu, \Sigma)$ where $X_1 = ... = X_n$, write a function named `conditional_distribution` to find the distribution of $X_i$ for $i=1, ..., n$ and return the parameters of the conditional distribution.
"""

def conditional_distribution(mu, sigma, n):
    """
    This function calculates the parameters of the conditional distribution of X_i 
    given that X_1 = ... = X_n in a multivariate normal distribution.

    Parameters:
    mu (float): The mean of the multivariate normal distribution.
    sigma (float): The variance of the multivariate normal distribution.
    n (int): The number of variables in the multivariate normal distribution.

    Returns:
    tuple: A tuple containing the mean and variance of the conditional distribution.
    """
    conditional_mean = mu
    conditional_variance = sigma / n
    return conditional_mean, conditional_variance