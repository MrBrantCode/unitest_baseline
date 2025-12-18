"""
QUESTION:
Write a function `square_sum_detector(val)` that takes an integer `val` as input and returns a tuple of two perfect squares whose sum equals `val` if such a pair exists; otherwise, return `False`. The function should only consider pairs where both squares are non-negative integers.
"""

def square_sum_detector(val):
    i = 0
    # Iterate from 0 to square root of val
    while i*i <= val:
        j = int((val - i*i)**0.5)
        if i*i + j*j == val:
            return (i*i, j*j)
        i += 1
    return False