"""
QUESTION:
Write a function `is_armstrong_number(num)` that takes a positive integer as input and returns `True` if the number is an Armstrong number, prime, and has exactly three unique digits, and `False` otherwise. The function should also handle error cases where the input is not a valid positive integer.
"""

import math

def is_armstrong_number(num):
    if not isinstance(num, int) or num <= 0:
        return False

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    # Check if the number is prime
    if not is_prime(num):
        return False

    # Check if the number has exactly three unique digits
    digits = set(str(num))
    if len(digits) != 3:
        return False

    # Calculate the sum of its digits raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))

    # Check if the sum is equal to the original number
    if sum_of_digits == num:
        return True
    else:
        return False