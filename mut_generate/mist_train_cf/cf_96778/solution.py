"""
QUESTION:
Write a function `sum_multiples` that calculates the sum of all the multiples of 7 and 11 between 0 and a given positive integer `n` (inclusive), where `n` is less than or equal to 100, using recursion and without using any loops or conditional statements (other than those used in the recursion itself).
"""

def sum_multiples(n):
    if n < 7:  # Base case: if n is less than 7, return 0
        return 0
    elif n % 7 == 0 or n % 11 == 0:  # Recursive case: if n is divisible by 7 or 11, add n to the sum
        return n + sum_multiples(n - 1)
    else:  # Recursive case: if n is not divisible by 7 or 11, continue recursively with n - 1
        return sum_multiples(n - 1)