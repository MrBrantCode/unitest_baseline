"""
QUESTION:
Write a function named `calculate_number_properties` that takes an array of numbers as input and returns an array of objects. Each object should have three properties: 'number', 'square_root', and 'factorial'. The 'square_root' should be rounded to the nearest whole number. The 'factorial' should be calculated using a recursive function.
"""

import math

def calculate_number_properties(numbers):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    result = []
    for num in numbers:
        obj = {
            'number': num,
            'square_root': round(math.sqrt(num)),
            'factorial': factorial(num)
        }
        result.append(obj)
    return result