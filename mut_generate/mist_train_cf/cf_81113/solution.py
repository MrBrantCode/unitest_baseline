"""
QUESTION:
Calculate the geometric mean of a list of numbers, replacing non-positive numbers with the arithmetic mean of the remaining positive numbers. The function `geometric_mean(numbers)` should take a list of numbers as input and return the geometric mean as output. If the list only contains non-positive numbers, return an error message.
"""

import math

def geometric_mean(numbers):
    n = len(numbers)
    positive_numbers = [num for num in numbers if num>0]
    if len(positive_numbers) == 0:
        return "Error: The list only contains non-positive numbers."
    else:
        arithmetic_mean = sum(positive_numbers)/len(positive_numbers)
        numbers = [num if num>0 else arithmetic_mean for num in numbers]
        product = math.prod(numbers)
        return pow(product, 1/n)