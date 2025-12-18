"""
QUESTION:
Write a function `sum_of_cubes(n)` that takes a positive integer `n` as input and returns the sum of the cubes of each digit in the number with a time complexity of O(n), where n is the number of digits in the input number. The input integer `n` must be a positive integer.
"""

def sum_of_cubes(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit**3
        n //= 10
    return total