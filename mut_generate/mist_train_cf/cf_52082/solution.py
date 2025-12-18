"""
QUESTION:
Design a function named `leading_zeros_in_factorial` that calculates the number of leading zeros in the binary representation of a factorial of a given integer `n`. The function should be efficient enough to handle large values of `n`.
"""

def leading_zeros_in_factorial(n):
    # Count no of trailing zeros in factorial
    count = 0
    i = 5
    while (n / i >= 1):
        count += int(n/i)
        i *= 5
    return count