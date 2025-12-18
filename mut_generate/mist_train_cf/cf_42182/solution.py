"""
QUESTION:
Write a function `is_armstrong_number(num)` that takes an integer `num` as input and returns `True` if the number is equal to the sum of its own digits each raised to the power of the number of digits, and `False` otherwise.
"""

def entance(num):
    num_str = str(num)
    num_digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
    return total == num