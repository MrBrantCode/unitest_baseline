"""
QUESTION:
Write a function called `find_gcd` that takes a list of numbers as input and returns their greatest common divisor. The function should handle lists of any length, including empty lists and lists with a single element.
"""

import math
def find_gcd(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        result = math.gcd(numbers[0], numbers[1])
        for i in range(2, len(numbers)):
            result = math.gcd(result, numbers[i])
        return result