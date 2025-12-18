"""
QUESTION:
Write a recursive function named `number_to_string(n)` that takes a positive integer `n` as input and returns its string representation.
"""

def number_to_string(n):
    if n < 10:
        return str(n)
    else:
        return number_to_string(n // 10) + str(n % 10)