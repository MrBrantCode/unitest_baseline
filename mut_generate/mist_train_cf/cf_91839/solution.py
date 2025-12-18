"""
QUESTION:
Write a function named `is_armstrong_number` that determines whether a given number is an Armstrong number or not, considering that the number must also be prime and have exactly three unique digits. The function should take one integer argument and return a boolean value. The number is considered prime if it is greater than 1 and has no divisors other than 1 and itself.
"""

import math

def is_armstrong_number(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    digit_set = set(str(n))
    if len(digit_set) != 3:
        return False
    return True