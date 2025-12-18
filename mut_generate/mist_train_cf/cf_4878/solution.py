"""
QUESTION:
Implement a function named `calculate_square_roots` that takes a list of elements as input, replaces numbers with their square roots, and returns the modified list. For decimal numbers, round them to the nearest whole number before calculating the square root. For negative numbers, calculate the square root as a complex number. Non-numeric elements should remain unchanged.
"""

import math

def calculate_square_roots(input_list):
    result = []
    
    for element in input_list:
        if isinstance(element, (int, float)):
            if element >= 0:
                sqrt = round(math.sqrt(element))
            else:
                sqrt = round(math.sqrt(abs(element))) * -1
                if isinstance(sqrt, int):
                    sqrt = complex(sqrt, 0)
            result.append(sqrt)
        else:
            result.append(element)
    
    return result