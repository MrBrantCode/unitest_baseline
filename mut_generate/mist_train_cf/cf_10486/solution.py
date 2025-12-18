"""
QUESTION:
Create a function named `sum_of_digits(n)` that calculates the sum of the digits of an integer `n`. The function should take one argument `n`, a non-zero integer, and return the sum of its digits. The function must handle both positive and negative integers.
"""

def sum_of_digits(n):
    sum = 0
    n = abs(n)
    n_str = str(n)
    for char in n_str:
        digit = int(char)
        sum += digit
    return sum