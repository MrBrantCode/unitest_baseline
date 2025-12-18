"""
QUESTION:
Write a function named `sum_odd_numbers(n)` that calculates the sum of all odd numbers up to `n` (inclusive), excluding any multiples of 3, using recursion. The function should take an integer `n` as input and return the sum as output.
"""

def sum_odd_numbers(n):
    # Base case: if n is 1, return 1 (the only odd number less than or equal to 1)
    if n == 1:
        return 1
    # Recursive case: if n is odd and not a multiple of 3, add it to the sum
    if n % 2 == 1 and n % 3 != 0:
        return n + sum_odd_numbers(n - 1)
    # Recursive case: if n is even or a multiple of 3, skip it and move to the next number
    else:
        return sum_odd_numbers(n - 1)