"""
QUESTION:
Estimate the prior probability of receiving a positive test result for disease D, given the sensitivity (0.99), specificity (0.97), and prevalence (0.05) of the diagnostic test. Implement the function `estimate_prior_probability` that takes sensitivity, specificity, and prevalence as inputs and returns the estimated prior probability.
"""

def estimate_prior_probability(sensitivity, specificity, prevalence):
    """
    Estimates the prior probability of receiving a positive test result for a given disease.

    Parameters:
    sensitivity (float): The true positive rate of the diagnostic test.
    specificity (float): The true negative rate of the diagnostic test.
    prevalence (float): The proportion of the population with the disease.

    Returns:
    float: The estimated prior probability of receiving a positive test result.
    """
    return (sensitivity * prevalence) / ((sensitivity * prevalence) + ((1 - specificity) * (1 - prevalence)))