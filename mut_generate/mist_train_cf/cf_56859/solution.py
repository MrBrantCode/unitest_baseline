"""
QUESTION:
Create a function named `create_beta_prior` that takes one argument `prior_probability` representing the prior belief of the probability of getting a head. The function should return two values, `alpha` and `beta`, such that `alpha / (alpha + beta)` equals `prior_probability`. Note that `alpha` and `beta` should be positive integers and their values should be the smallest possible that satisfy the condition.
"""

def create_beta_prior(prior_probability):
    """
    Returns the smallest possible positive integer values of alpha and beta 
    such that alpha / (alpha + beta) equals prior_probability.

    Args:
        prior_probability (float): The prior belief of the probability of getting a head.

    Returns:
        tuple: A tuple of two integers, alpha and beta.
    """
    alpha = int(prior_probability * 10)  # Multiply by 10 to get the smallest possible integer value
    beta = 10 - alpha
    return alpha, beta