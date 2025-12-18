"""
QUESTION:
Write a function `get_max_values(d)` that takes a dictionary `d` as input where the keys are strings and the values are positive integers. The function should return a dictionary where the keys are the same as the input dictionary, and the values are the maximum values from the input dictionary that are divisible by 3 and have at least one prime factor, otherwise, return 0 for that key.
"""

import math

def is_divisible_by_3(n):
    return n % 3 == 0

def has_prime_factor(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return True
    return False

def get_max_values(d):
    max_values = {}
    
    for key, value in d.items():
        if isinstance(value, int) and is_divisible_by_3(value) and has_prime_factor(value):
            if key not in max_values or value > max_values[key]:
                max_values[key] = value
        else:
            max_values[key] = 0
    
    return max_values