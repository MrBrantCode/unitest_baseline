"""
QUESTION:
Implement a function named `beta_binomial_bayes` that uses the Bayesian Filter approach to estimate the probability of a system failing based on observations, utilizing the Beta distribution for the prior probability and the Binomial distribution for the likelihood function, and returns the posterior Beta distribution.
"""

def beta_binomial_bayes(prior_alpha, prior_beta, num_trials, num_successes):
    """
    Calculate the posterior Beta distribution parameters after observing num_trials and num_successes.

    Args:
        prior_alpha (float): The alpha parameter of the prior Beta distribution.
        prior_beta (float): The beta parameter of the prior Beta distribution.
        num_trials (int): The total number of trials observed.
        num_successes (int): The number of successful trials.

    Returns:
        tuple: A tuple containing the alpha and beta parameters of the posterior Beta distribution.
    """

    # Calculate the posterior alpha and beta parameters using the conjugate prior property
    posterior_alpha = prior_alpha + num_successes
    posterior_beta = prior_beta + num_trials - num_successes

    return posterior_alpha, posterior_beta