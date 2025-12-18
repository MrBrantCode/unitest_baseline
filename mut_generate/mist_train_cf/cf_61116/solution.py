"""
QUESTION:
Find the least square estimator for the parameter p in a binomial distribution Bin(n, p). The function should take the number of trials (n) and the number of successes (x) as input, and return the estimated value of p.
"""

def binomial_estimator(n, x):
    """
    This function calculates the least square estimator for the parameter p in a binomial distribution Bin(n, p).
    
    Parameters:
    n (int): The number of trials.
    x (int): The number of successes.
    
    Returns:
    float: The estimated value of p.
    """
    return x / n