"""
QUESTION:
Write a recursive function named `number_to_string` that converts a positive integer into a string. The function must only take one argument `n`, a positive integer, and return the string representation of `n`.
"""

def number_to_string(n):
    if n < 10:
        return str(n)
    else:
        return number_to_string(n // 10) + str(n % 10)