"""
QUESTION:
Write a function `max_consecutive_ones` that takes an integer `n` as input and returns the maximum number of consecutive 1s in the binary representation of the integer `n`.
"""

def max_consecutive_ones(n):
    max_ones = 0
    current_ones = 0

    while n > 0:
        if n % 2 == 1:
            current_ones += 1
            max_ones = max(max_ones, current_ones)
        else:
            current_ones = 0
        n //= 2

    return max_ones