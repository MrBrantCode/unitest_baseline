"""
QUESTION:
Calculate the variance between observed and expected digit frequencies according to Benford's Law. Given the observed frequencies of digits (`f_d_observed`) and the expected frequencies (`f_d_expected`), write a function `calculate_variance` that takes in a list of observed frequencies and the total number of observations, and returns the variance between the observed and expected frequencies. The expected frequencies should be calculated by multiplying the Benford's Law probabilities by the total number of observations.
"""

def calculate_variance(f_d_observed, total_observations):
    """
    Calculate the variance between observed and expected digit frequencies according to Benford's Law.

    Args:
    f_d_observed (list): A list of observed frequencies of digits.
    total_observations (int): The total number of observations.

    Returns:
    float: The variance between the observed and expected frequencies.
    """
    benford_probabilities = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
    f_d_expected = [p * total_observations for p in benford_probabilities]
    
    variance = sum((obs - exp) ** 2 for obs, exp in zip(f_d_observed, f_d_expected))
    return variance