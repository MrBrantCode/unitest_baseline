"""
QUESTION:
Create a function `is_armstrong_number(num)` that takes an integer `num` as input and returns `True` if it is an Armstrong number that is also prime, has exactly three unique digits, and the sum of its digits raised to the power of the number of digits equals the original number. The function should return `False` for invalid inputs that are not positive integers.
"""

import math

def is_armstrong_number(num):
    if not isinstance(num, int) or num <= 0:
        return False

    # Check if the number is prime
    if not (num > 1 and all(num % i for i in range(2, int(math.sqrt(num)) + 1))):
        return False

    # Check if the number has exactly three unique digits
    digits = set(str(num))
    if len(digits) != 3:
        return False

    # Calculate the sum of its digits raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))

    # Check if the sum is equal to the original number
    return sum_of_digits == num