"""
QUESTION:
Create a function `digit_sum` that takes an integer `n` as input and returns the sum of all digits of `n` in O(log n) time complexity, where n is the given integer. The function should work with non-negative integers.
"""

def digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + digit_sum(n // 10)