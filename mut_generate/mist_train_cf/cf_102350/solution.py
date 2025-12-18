"""
QUESTION:
Create a function `transform_list` that takes a list of integers as input. For each integer in the list, if the number is even, multiply it by 3; if the number is odd, replace it with the square root of the number rounded to the nearest integer. Return the transformed list.
"""

import math

def transform_list(lst):
    transformed_lst = []
    
    for num in lst:
        if num % 2 == 0:  # even number
            transformed_lst.append(num * 3)
        else:  # odd number
            transformed_lst.append(round(math.sqrt(num)))
    
    return transformed_lst