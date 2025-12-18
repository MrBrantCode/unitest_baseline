"""
QUESTION:
Implement a function `calculate_spearman_correlation` that calculates the Spearman rank correlation coefficient between two lists of numerical values. The function should take two lists of floats as input and return the Spearman rank correlation coefficient as a float. The Spearman rank correlation coefficient is calculated using the formula `rs = 1 - (6 * sum(di^2)) / (n * (n^2 - 1))`, where `di` is the difference between the ranks of corresponding variables and `n` is the number of observations. The function should handle lists of the same length.
"""

from typing import List
import numpy as np

def calculate_spearman_correlation(list1: List[float], list2: List[float]) -> float:
    n = len(list1)
    ranks1 = np.argsort(np.argsort(list1))
    ranks2 = np.argsort(np.argsort(list2))
    d_squared = np.sum((ranks1 - ranks2) ** 2)
    spearman_coefficient = 1 - (6 * d_squared) / (n * (n**2 - 1))
    return spearman_coefficient