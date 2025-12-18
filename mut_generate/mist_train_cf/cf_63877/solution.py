"""
QUESTION:
Write a function `compare_number_arrays_order` that compares two input strings and returns `True` if they contain the same sequence of distinct numerical values (including decimal points and negative integers), excluding non-digit characters, and `False` otherwise.
"""

import re

def compare_number_arrays_order(string1: str, string2: str):
    # Use regular expressions to find all the numbers in the strings.
    numbers1 = re.findall(r"-?\d+\.?\d*", string1)
    numbers2 = re.findall(r"-?\d+\.?\d*", string2)

    # Since the numbers are returned as strings, we'll convert them to floats for comparison.
    numbers1 = [float(num) for num in numbers1]
    numbers2 = [float(num) for num in numbers2]

    # Compare the sequences. If they are the same, return True. Else, return False.
    return numbers1 == numbers2