"""
QUESTION:
Write a Python function named `is_armstrong_number` that determines if a given integer `num` is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. The function should return `True` if the number is an Armstrong number and `False` otherwise.
"""

def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    armstrong_sum = sum(int(digit) ** power for digit in num_str)
    return armstrong_sum == num