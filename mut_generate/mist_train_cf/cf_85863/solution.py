"""
QUESTION:
Implement a function named `bayesian_inference` that takes in two parameters: `prior_prob` (representing the prior probability) and `likelihood` (representing the likelihood of the data). Combine the prior knowledge with the machine learning probability prediction results using Bayes' rule and return the resulting posterior probability.
"""

def bayesian_inference(prior_prob, likelihood):
    """
    Combines prior knowledge with machine learning probability prediction results using Bayes' rule.

    Args:
        prior_prob (float): The prior probability.
        likelihood (float): The likelihood of the data.

    Returns:
        float: The resulting posterior probability.
    """
    # Calculate the posterior probability using Bayes' rule
    # For simplicity, we assume the evidence is 1, as it is not provided in the problem
    posterior_prob = (likelihood * prior_prob) / 1
    
    return posterior_prob