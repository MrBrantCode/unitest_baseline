"""
QUESTION:
Given an undisclosed integer t chosen randomly within the range 1 ≤ t ≤ n, calculate the difference in the expected number of guesses required to discover t using a standard binary search and a random binary search, rounded to 8 decimal places, for n = 10^10.
"""

import math
import numpy as np

def entrance(n):
    B_n = math.log2(n) + 1
    R_n = 2 * np.log(n)
    return round(R_n - B_n, 8)