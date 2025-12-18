"""
QUESTION:
Create a function `polynomial_occur` that takes a non-empty list of positive integers as input and returns the smallest integer that appears at a frequency corresponding to a polynomial function (e.g., 2^x, x^2). If multiple integers meet this criterion, return the smallest one. If no such integer exists, return -1.
"""

import collections
import math

def polynomial_occur(arr):
    count_elements = collections.Counter(arr)
    polynomial_freq_nums = sorted([num for num, freq in count_elements.items() if freq > 1 and
                                   any(math.isclose(freq, base**power, rel_tol=1e-5) for base in range(2, int(freq**0.5)+1)
                                       for power in range(2, int(math.log(freq, 2))+1))])
    return polynomial_freq_nums[0] if polynomial_freq_nums else -1