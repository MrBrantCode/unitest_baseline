"""
QUESTION:
Scale a vector of evenly spaced numbers from 0 to 1000 using a prime number as the scaling factor. The function should be named `scale_vector` and take a list of numbers as input. The scaling factor should be a prime number larger than 1000. The output vector should contain the scaled numbers, rounded to the nearest integer.
"""

import math

def scale_vector(input_vector):
    scaling_factor = 1019 / 1000
    output_vector = [round(num * scaling_factor) for num in input_vector]
    return output_vector