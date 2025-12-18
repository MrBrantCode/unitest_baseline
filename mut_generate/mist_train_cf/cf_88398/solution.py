"""
QUESTION:
Write a function named `build_array` that takes an array of integers as input, where each integer is between 1 and 10 inclusive. The function should return an array of objects, where each object contains the original number, its square root rounded to the nearest whole number, and its factorial calculated using a recursive function.
"""

import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def build_array(numbers):
    result = []
    for number in numbers:
        square_root = round(math.sqrt(number))
        fact = factorial(number)
        obj = {
            'number': number,
            'square_root': square_root,
            'factorial': fact
        }
        result.append(obj)
    return result