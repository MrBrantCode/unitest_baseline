"""
QUESTION:
Write a function called `mle_lambda` that calculates the maximum likelihood estimate (MLE) of the parameter λ for an exponential distribution. The function should take as input a list of observed lifetimes `x` of length `n`, where each lifetime is a non-negative number. The function should return a single number representing the MLE of λ. The function should assume that the observed lifetimes are independent and identically distributed (i.i.d.) and that the lifetime of each component follows an exponential distribution with parameter λ.
"""

def mle_lambda(x):
    """
    This function calculates the maximum likelihood estimate (MLE) of the parameter λ 
    for an exponential distribution.

    Args:
    x (list): A list of observed lifetimes of length n, where each lifetime is a non-negative number.

    Returns:
    float: The MLE of λ.
    """
    n = len(x)
    return n / sum(x)