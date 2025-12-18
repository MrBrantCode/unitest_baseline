"""
QUESTION:
Create a function `scale_vector` that takes a list of evenly spaced numbers from 0 to 100 as input and returns a new list where each number in the input list is scaled by a prime number. The output list should also contain 20 numbers.
"""

import math

def scale_vector(input_vector):
    scaling_factor = 101
    output_vector = [round(i * scaling_factor) for i in input_vector]
    return output_vector