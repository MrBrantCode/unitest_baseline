"""
QUESTION:
Write a function `is_armstrong_number(n)` to check if a given number `n` is an Armstrong number. An Armstrong number is a number when the sum of the cubes of its own digits is equal to the number itself. The function should take an integer `n` as input and return `True` if it's an Armstrong number, `False` otherwise.
"""

def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_cubes = 0
    for i in range(num_digits):
        digit = int(num_str[i])
        sum_cubes += digit**num_digits
    return sum_cubes == n