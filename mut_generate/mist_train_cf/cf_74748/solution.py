"""
QUESTION:
Create a function `calculate_hcf` that takes an array of integers as input and returns their highest common factor (HCF). The function should include error checking to ensure that only positive integers are used in the calculation. If any input is not a positive integer, the function should return an error message.
"""

from functools import reduce
from math import gcd

def calculate_hcf(numbers):
    # Ensure all inputs are integers and positive
    for i in numbers:
        if not isinstance(i, int) or i < 1:
            return "Error: all numbers must be positive integers."

    return reduce(lambda x,y: gcd(x,y), numbers)  # Use the reduce function to calculate the hcf