"""
QUESTION:
Write a function `conditional_binomial_distribution` that calculates the parameters of the conditional distribution of X given X+Y, where X and Y are independent Binomial random variables with parameters (n1, p) and (n2, q) respectively. The function should return the parameters (number of trials, success probability) of the resulting Binomial distribution.
"""

def conditional_binomial_distribution(n1, p, n2, q):
    """
    Calculate the parameters of the conditional distribution of X given X+Y,
    where X and Y are independent Binomial random variables with parameters 
    (n1, p) and (n2, q) respectively.

    Args:
        n1 (int): Number of trials for X.
        p (float): Success probability for X.
        n2 (int): Number of trials for Y.
        q (float): Success probability for Y.

    Returns:
        tuple: The parameters (number of trials, success probability) of the 
        resulting Binomial distribution.
    """
    # Calculate the number of trials for the conditional distribution
    conditional_n = n1 + n2
    
    # Calculate the success probability for the conditional distribution
    conditional_p = p / (p + q)
    
    return conditional_n, conditional_p