"""
QUESTION:
Write a function named `calculate_posterior_probability` to compute the posterior probability of a person suffering from a disease given a positive test result, using the incidence rate of the disease and the accuracy of the medical diagnostic examination. The function should take the incidence rate of the disease and the probabilities of the test indicating a positive result for an afflicted person and a negative result for an unafflicted person as input.
"""

def calculate_posterior_probability(incidence_rate, prob_positive_given_disease, prob_negative_given_no_disease):
    """
    Calculate the posterior probability of a person suffering from a disease given a positive test result.

    Parameters:
    incidence_rate (float): The incidence rate of the disease.
    prob_positive_given_disease (float): The probability of the test indicating a positive result for an afflicted person.
    prob_negative_given_no_disease (float): The probability of the test indicating a negative result for an unafflicted person.

    Returns:
    float: The posterior probability of a person suffering from a disease given a positive test result.
    """
    prob_positive = prob_positive_given_disease * incidence_rate + (1 - prob_negative_given_no_disease) * (1 - incidence_rate)
    posterior_probability = prob_positive_given_disease * incidence_rate / prob_positive
    return posterior_probability