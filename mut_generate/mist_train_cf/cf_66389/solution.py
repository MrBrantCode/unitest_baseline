"""
QUESTION:
Write a function `multiply_abs_values_v3` that takes a list of floating-point numbers as input and returns the product of their absolute values, with certain conditions applied. 

The function should consider the closest inferior integer for each number. Negative numbers with decimal parts equal to or over 0.5 should be considered positive. Numbers that are divisible by any prime number smaller than 10 (2, 3, 5, 7) should be excluded from the computation. Negative zero should be treated as a unique value and included in the product.
"""

import math

def multiply_abs_values_v3(lst):
    product = 1
    abs_values = []
    for i in lst:
        if i <= -0.5:
            i = -i
            if all(i % j != 0 for j in [2, 3, 5, 7]):
                abs_values.append(math.floor(i)+1)
        elif i < 0 and i > -0.5:
            abs_values.append(0)
        else:
            if all(i % j != 0 for j in [2, 3, 5, 7]):
                abs_values.append(math.floor(i))
                        
    for i in abs_values:
        product *= i
    return product