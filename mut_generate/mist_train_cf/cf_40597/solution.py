"""
QUESTION:
Implement a function `count_divisible_numbers(x, y, k)` that returns the count of integers within the range `[x, y]` (inclusive) that are divisible by `k`. The function should not use division and modulo operations.
"""

def count_divisible_numbers(x, y, k):
    if x % k == 0:
        return (y - x) // k + 1
    else:
        return (y // k + 1) - (x // k + 1)