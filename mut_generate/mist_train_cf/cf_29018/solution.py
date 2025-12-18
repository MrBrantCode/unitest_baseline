"""
QUESTION:
Write a function `modify_list` that takes a list of integers as input and returns a list containing the squares of all the even numbers in the input list, in the same order as they appear in the input list. If the input list is empty or does not contain any even numbers, the function should return an empty list.
"""

from typing import List

def modify_list(arr: List[int]) -> List[int]:
    return [x**2 for x in arr if x % 2 == 0]