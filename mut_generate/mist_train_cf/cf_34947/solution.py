"""
QUESTION:
Write a function `reverse_list_to_string` that takes a list of integers as its parameter and returns a string representation of the list in reverse order. The function should reverse the list and then convert each element to a string before joining them together into a single string.
"""

from typing import List

def reverse_list_to_string(input_list: List[int]) -> str:
    reversed_list = list(map(str, reversed(input_list)))
    return "".join(reversed_list)