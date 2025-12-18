"""
QUESTION:
Write a function `lcm_list(numbers)` to calculate the least common multiple (LCM) of a list of numbers using the prime factorization method. This function should take a list of integers as input and return their LCM as an integer. The function should also utilize a helper function `lcm(a, b)` to calculate the LCM of two numbers.
"""

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result