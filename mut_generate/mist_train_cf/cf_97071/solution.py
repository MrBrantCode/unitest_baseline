"""
QUESTION:
Create a function named `is_armstrong_number(n)` that checks whether a given number `n` is an Armstrong number or not. An Armstrong number is a number that is equal to the sum of the cubes of its own digits. The function should return `True` if `n` is an Armstrong number and `False` otherwise.
"""

def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_cubes = 0
    for i in range(num_digits):
        digit = int(num_str[i])
        sum_cubes += digit**num_digits
    return sum_cubes == n