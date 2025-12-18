"""
QUESTION:
In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number. Numbers will not have leading zeros. 

For example, `solve("gh12cdy695m1") = 695`, because this is the largest of all number groupings. 

Good luck!

Please also try [Simple remove duplicates](https://www.codewars.com/kata/5ba38ba180824a86850000f7)
"""

import re

def find_largest_number(s: str) -> int:
    """
    Finds the largest number in a string that contains lowercase letters and numbers.

    Parameters:
    s (str): A string containing lowercase letters and numbers.

    Returns:
    int: The largest number found in the string.
    """
    return max(map(int, re.findall('(\\d+)', s)))