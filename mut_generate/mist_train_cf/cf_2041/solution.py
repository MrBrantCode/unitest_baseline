"""
QUESTION:
Create a class with a method named `round_sum` that takes an array as input, calculates the sum of its elements (considering only the real part of complex numbers), and returns the sum rounded to the nearest integer. The method should have a time complexity of O(n), where n is the number of elements in the array. The array can contain negative numbers, floating-point numbers, and complex numbers.
"""

import math

def round_sum(arr):
    total = 0
    for num in arr:
        if isinstance(num, complex):
            total += num.real
        else:
            total += num

    return round(total)