"""
QUESTION:
Write a function called `build_array` that takes an array of positive integers as input and returns a new array of objects. Each object in the array should contain three properties: the number itself, its square root rounded to the nearest whole number, and its factorial calculated using a recursive function. The input array will only contain numbers between 1 and 10 inclusive.
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