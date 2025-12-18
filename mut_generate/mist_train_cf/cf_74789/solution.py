"""
QUESTION:
Write a function `digit_sum_prime` that takes an integer `n` as input, calculates the sum of its digits, and checks if the sum is a prime number. The function should return the sum of the digits and a boolean indicating whether the sum is prime. The input integer is guaranteed to be non-negative.
"""

import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def digit_sum_prime(n): 
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum, is_prime(digit_sum)