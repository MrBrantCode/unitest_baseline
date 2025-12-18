"""
QUESTION:
Implement a function `getMaxExpArray` that calculates the maximum exponent array for a given precision. The function should take an integer `max_precision` as input and return an array of length `max_precision + 1` containing uint256 values. The first element of the array should be `0x386bfdba29`, and each subsequent element should be calculated as the previous element plus `0x38d1b71758` times the element's index.
"""

def getMaxExpArray(max_precision):
    maxExpArray = [0] * (max_precision + 1)
    maxExpArray[0] = 0x386bfdba29
    for i in range(1, max_precision + 1):
        maxExpArray[i] = maxExpArray[i - 1] + (0x38d1b71758 * i)
    return maxExpArray