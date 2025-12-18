"""
QUESTION:
Design a function `polynomial_occur(arr)` that takes a non-empty list of positive integers as input. The function should return the smallest integer that occurs at a polynomial frequency (either a perfect square or a power of 2) in the list. If multiple integers meet this condition, return the smallest one. If no such integer is found, return -1.
"""

import math
from collections import Counter

def polynomial_occur(arr):
    # frequency dictionary
    frequency = Counter(arr)

    def isPerfectSquare(x):
        return x == math.isqrt(x) ** 2

    def isPowerOfTwo(n):
        return (n and (not(n & (n - 1))))

    # list to store numbers with polynomial frequency
    polynomial_frequency = []

    for num, freq in frequency.items():
        # if freq is perfect square or power of 2, append num to list
        if isPerfectSquare(freq) or isPowerOfTwo(freq):
            polynomial_frequency.append(num)

    # if list is not empty, return smallest number. Else, return -1
    if polynomial_frequency:
        return min(polynomial_frequency)
    else:
        return -1