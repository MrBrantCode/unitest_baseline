"""
QUESTION:
Given a list of integers representing submission results where 1 is correct and 0 is incorrect, write a function `find_first_incorrect` that returns the index of the first incorrect submission (0). If all submissions are correct, return -1.

The function should take a list of integers as input and return an integer representing the index of the first incorrect submission or -1 if all submissions are correct.
"""

from typing import List

def find_first_incorrect(submissions: List[int]) -> int:
    for i in range(len(submissions)):
        if submissions[i] == 0:
            return i
    return -1