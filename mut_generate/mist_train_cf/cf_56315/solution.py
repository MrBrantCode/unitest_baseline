"""
QUESTION:
Write a function `gcd_of_lists` that takes two lists of integers as input. Each integer in the lists should be greater than zero and less than or equal to 1000. The function should return the Greatest Common Divisor (GCD) of all integers in both lists.
"""

import math
from functools import reduce

def gcd_of_lists(list1, list2):
    """
    Calculate the Greatest Common Divisor (GCD) of all integers in two lists.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        int: The GCD of all integers in both lists.
    """
    def gcd_of_list(lst):
        return reduce(math.gcd, lst)

    gcd_list1 = gcd_of_list(list1)
    gcd_list2 = gcd_of_list(list2)
    
    return math.gcd(gcd_list1, gcd_list2)