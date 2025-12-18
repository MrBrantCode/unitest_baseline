"""
QUESTION:
Write a function `get_max_values(d)` that takes a dictionary `d` as input, where `d` contains only positive integers as values. The function should return a new dictionary where each key is the same as in the input dictionary, and each value is the maximum value for that key if the value is an integer, divisible by 3, and contains a prime number in its prime factorization; otherwise, the value should be 0.
"""

import math

def is_divisible_by_3(n):
    return n % 3 == 0

def has_prime_factor(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return True
    return False

def entrance(d):
    max_values = {}
    
    for key, value in d.items():
        if isinstance(value, int) and is_divisible_by_3(value) and has_prime_factor(value):
            if key not in max_values or value > max_values[key]:
                max_values[key] = value
        else:
            max_values[key] = 0
    
    return max_values