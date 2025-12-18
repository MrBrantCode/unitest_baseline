"""
QUESTION:
Write a function `calculate_difference` that takes two numbers `num1` and `num2` as input and returns their difference. The difference should only be calculated if `num1` is larger than `num2`. If `num1` is smaller or equal to `num2`, the function should return a message stating that the difference cannot be calculated.

If `num1` is a prime number, the difference should be calculated using the absolute values of the two numbers. If `num1` is not a prime number, the difference should be calculated using the negative difference of the two numbers. If the calculated difference can be evenly divided by 2, the function should return the result divided by 2. If the difference cannot be evenly divided by 2, the function should return the result multiplied by 2.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def calculate_difference(num1, num2):
    if num1 <= num2:
        return "The difference cannot be calculated."

    if is_prime(num1):
        difference = abs(num1 - num2)
    else:
        difference = -(num1 - num2)

    if difference % 2 == 0:
        return difference // 2
    else:
        return difference * 2