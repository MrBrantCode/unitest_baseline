"""
QUESTION:
Write a function `multiply_abs_values_v3(lst)` that takes a list of floating-point numbers as input. The function should return the product of the absolute values, determined based on the closest floor integers, but negative floats with a decimal part equal to or exceeding 0.5 should be treated as positive. Additionally, exclude items divisible by any prime number less than 10 from the calculation. If the list contains negative zero as an integer (-0), it should be seen as a unique value and factored into the product result.
"""

import math
from functools import reduce

PRIMES_LESS_THAN_TEN = [2, 3, 5, 7]

def multiply_abs_values_v3(lst):
    def apply_rules(value):
        closest_integer = math.floor(value) if value >= 0 else math.ceil(value)
        is_prime_divisible = any(closest_integer % prime == 0 for prime in PRIMES_LESS_THAN_TEN)

        if closest_integer == 0 and value < 0:  
            return -1
        
        if is_prime_divisible or (closest_integer < 0 and value - closest_integer >= 0.5):
            return 1
        else:
            return abs(closest_integer)

    return reduce(lambda a, b: a * b, [apply_rules(value) for value in lst])