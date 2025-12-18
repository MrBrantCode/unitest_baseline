"""
QUESTION:
Write a function called `calculate_geometric_mean` that calculates the geometric mean of a list of numbers. The function should take a list of positive numbers as input and return the geometric mean as a floating-point number. The input list is not empty and all elements are positive numbers.
"""

import math

def calculate_geometric_mean(num_list):
    product = 1
    for num in num_list:
        product *= num
    geometric_mean = math.pow(product, 1/len(num_list))
    return geometric_mean