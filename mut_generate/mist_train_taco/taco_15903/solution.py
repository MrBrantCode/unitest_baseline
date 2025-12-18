"""
QUESTION:
Your task in this kata is to implement a function that calculates the sum of the integers inside a string. For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.

*Note: only positive integers will be tested.*
"""

import re

def sum_of_integers_in_string(s: str) -> int:
    """
    Calculates the sum of all integers found within the given string.

    Parameters:
    s (str): The input string containing integers.

    Returns:
    int: The sum of all integers found in the string.
    """
    return sum((int(x) for x in re.findall(r'\d+', s)))