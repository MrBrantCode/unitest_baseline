"""
QUESTION:
Implement a function `calculate_sum` that takes a list of integers as input and returns the sum of all the numbers in the list using the reduce() function. The input list will contain at least one integer. Do not use any loops or the built-in sum() function. The function should have the following signature: `def calculate_sum(numbers: List[int]) -> int:`
"""

from functools import reduce
from typing import List

def calculate_sum(numbers: List[int]) -> int:
    return reduce(lambda x, y: x + y, numbers)