"""
QUESTION:
Create a function `gcd_array` that calculates the Greatest Common Divisor (GCD) of an inputted list of integers. The function should be able to handle lists of up to 10^5 elements, where each element is an integer between 1 and 10^9 (inclusive).
"""

from math import gcd
from functools import reduce
from typing import List

def gcd_array(numbers: List[int]) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of an inputted list of integers.

    Args:
        numbers (List[int]): A list of integers between 1 and 10^9 (inclusive).

    Returns:
        int: The GCD of all numbers in the input list.
    """
    return reduce(gcd, numbers)