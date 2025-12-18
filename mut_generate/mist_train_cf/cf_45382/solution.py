"""
QUESTION:
A function called `expected_rolls_per_year` is needed, where it calculates the expected number of times a balanced six-sided die needs to be rolled in a non-leap year. The die is rolled once a day, but if a 1 is rolled, it is re-rolled until a different number is obtained. The function should return the expected number of rolls in a non-leap year (365 days) based on the described rolling rule.
"""

import numpy as np

def expected_rolls_per_year(days: int = 365) -> float:
    outcomes = np.array([2, 3, 5, 4, 6, 1])
    probabilities = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

    expectation = np.sum(outcomes * probabilities)
    adjusted_expectation = expectation / (1 - 1/6)
    rolls_per_year = adjusted_expectation * days
    return rolls_per_year