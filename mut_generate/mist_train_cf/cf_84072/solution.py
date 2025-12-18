"""
QUESTION:
Construct a function `non_zero_digit_in_factorial` that takes a positive integer `n` as input and returns the last non-zero digit in the factorial of `n`. The function should be able to handle large values of `n` without overflowing.
"""

def non_zero_digit_in_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        while factorial % 10 == 0:    # remove all trailing zeros
            factorial //= 10
        factorial %= 1000000000       # limit the size of factorial to prevent overflow
    return factorial % 10