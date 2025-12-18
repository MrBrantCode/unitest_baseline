"""
QUESTION:
Implement a function `modify_list(zero_to_seven: List[int]) -> List[int]` that takes a list of integers from 0 to 7, removes all odd numbers, squares each remaining number, and returns the modified list in ascending order. The input list will always contain integers from 0 to 7.
"""

from typing import List

def entance(zero_to_seven: List[int]) -> List[int]:
    modified_list = [x**2 for x in zero_to_seven if x % 2 == 0]
    modified_list.sort()
    return modified_list