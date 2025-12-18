"""
QUESTION:
Write a function named `check_number_parity` that takes an integer `n` as input and returns a string indicating whether the number is even, odd, or neither (in the case of zero). The function should handle both positive and negative integers.
"""

def check_number_parity(n):
    if n == 0:
        return 'Zero is neither even nor odd'
    elif n < 0:
        n = -n
    if n % 2 == 0:
        return 'The number is even'
    else:
        return 'The number is odd'