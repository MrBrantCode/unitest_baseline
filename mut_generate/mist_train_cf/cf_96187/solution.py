"""
QUESTION:
Write a function `scale_vector` that takes a list of 20 evenly spaced numbers from 0 to 100 as input, scales each number by a prime number, and returns the scaled list. The prime number should be used as the scaling factor.
"""

import math

def scale_vector(numbers):
    scaling_factor = 101
    output_vector = [round(num * scaling_factor) for num in numbers]
    return output_vector