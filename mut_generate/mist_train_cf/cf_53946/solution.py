"""
QUESTION:
Write a function `calculate_posterior_probability` to determine the posterior probability of an individual being afflicted by a specific disease given a positive medical diagnostic test result. The function should take as input the disease prevalence rate, the probability of testing positive if the individual has the disease, and the probability of testing negative if the individual does not have the disease. The function should return the posterior probability as a decimal value.
"""

def calculate_posterior_probability(disease_prevalence, test_positive_given_disease, test_negative_given_no_disease):
    """
    Calculate the posterior probability of an individual being afflicted by a specific disease given a positive medical diagnostic test result.

    Args:
        disease_prevalence (float): The prevalence rate of the disease.
        test_positive_given_disease (float): The probability of testing positive if the individual has the disease.
        test_negative_given_no_disease (float): The probability of testing negative if the individual does not have the disease.

    Returns:
        float: The posterior probability as a decimal value.
    """

    # Calculate the probability of testing positive if the person does not have the disease
    test_positive_given_no_disease = 1 - test_negative_given_no_disease

    # Calculate the probability of not having the disease
    no_disease_prevalence = 1 - disease_prevalence

    # Apply Bayes' theorem to calculate the posterior probability
    posterior_probability = (test_positive_given_disease * disease_prevalence) / ((test_positive_given_disease * disease_prevalence) + (test_positive_given_no_disease * no_disease_prevalence))

    return posterior_probability