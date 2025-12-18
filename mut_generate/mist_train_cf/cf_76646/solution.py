"""
QUESTION:
Implement a function `square_and_factorial(nums)` that takes a list of integers `nums` and returns a tuple of two lists. The first list should contain the squares of each element in `nums`, and the second list should contain the factorial of each element in `nums`. The function should be able to handle edge cases, including an empty list and a list with a single element.
"""

import math

def square_and_factorial(nums):
    squares = [num ** 2 for num in nums]
    factorials = [math.factorial(num) for num in nums]
    return squares, factorials