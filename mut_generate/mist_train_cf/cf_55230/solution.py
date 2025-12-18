"""
QUESTION:
Calculate the probability of committing at least one Type I error in multiple independent hypothesis tests. 

Write a function called `calculate_type_i_error_probability` that takes two parameters: `n` (the number of tests) and `alpha` (the significance level of each test), and returns the probability of committing at least one Type I error in any of the tests. Assume that the tests are independent and each test has a probability of committing a Type I error equal to `alpha`.
"""

import math

def calculate_type_i_error_probability(n, alpha):
    """
    Calculate the probability of committing at least one Type I error in multiple independent hypothesis tests.

    Parameters:
    n (int): The number of tests.
    alpha (float): The significance level of each test.

    Returns:
    float: The probability of committing at least one Type I error in any of the tests.
    """
    prob_no_error_each_test = 1 - alpha
    prob_no_error_all_tests = math.pow(prob_no_error_each_test, n)
    return 1 - prob_no_error_all_tests