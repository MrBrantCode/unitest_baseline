"""
QUESTION:
Implement a function called `geometric_mean` that takes a two-dimensional array of numbers as input and calculates the geometric mean of the provided set of numbers. The function should ignore non-numeric values and negative numbers (including zero) in the calculation. If all numbers in the array are non-numeric, negative, or zero, the function should return None.
"""

import math

def geometric_mean(arr):
    product = 1
    count = 0
    for sublist in arr:
        for num in sublist:
            if isinstance(num, (int, float)) and num > 0:
                product *= num
                count += 1
    if count > 0:
        power = 1 / count
        return math.pow(product, power)
    else:
        return None