"""
QUESTION:
Create a function `is_perfect_square` that takes a list of integers as input and returns a new list where each element is a boolean indicating whether the corresponding number in the input list is a perfect square or not. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of integers in the input list. The input list can contain up to 10^6 integers, and each integer will be between 1 and 10^12.
"""

import math

def is_perfect_square(numbers):
    results = []
    for num in numbers:
        sqrt = math.sqrt(num)
        if int(sqrt) == sqrt:
            results.append(True)
        else:
            results.append(False)
    return results