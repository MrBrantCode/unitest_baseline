"""
QUESTION:
Write a function `ratio_divisible_by_three(arr)` that calculates the ratio of elements in a numeric array that are divisible by 3. The array will consist of integers ranging from 1 to 10^6 and the function should efficiently handle large inputs.
"""

import numpy as np

def ratio_divisible_by_three(arr):
    divisible_by_three = np.count_nonzero(arr % 3 == 0)
    ratio = divisible_by_three / len(arr)
    return ratio