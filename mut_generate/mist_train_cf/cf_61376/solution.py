"""
QUESTION:
Create a function `product_of_odds` that takes two parameters `first_number` and `last_number` where `first_number` is less than or equal to `last_number`. The function should calculate the product of all odd numbers within the given range (inclusive of endpoints). If `first_number` or `last_number` are not integers, round `first_number` up and `last_number` down to the nearest integer. The function should return the calculated product.
"""

import math

def product_of_odds(first_number, last_number):
    first_number = math.ceil(first_number)
    last_number = math.floor(last_number)

    product = 1
    for i in range(first_number, last_number + 1):  
        if i % 2 != 0:
            product *= i
    return product