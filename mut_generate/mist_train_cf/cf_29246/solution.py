"""
QUESTION:
Given a list of integers representing a chocolate bar, a target sum `d`, and a target segment length `m`, write a function `birthday(s, d, m)` to determine the number of ways the chocolate bar can be divided into segments of length `m` such that the sum of the integers in each segment equals `d`. The function should return the number of such divisions.

Constraints: The length of the chocolate bar is between 1 and 100, each segment has between 1 and 5 integers, `d` is between 1 and 31, and `m` is between 1 and 12.
"""

from typing import List

def entrance(s: List[int], d: int, m: int) -> int:
    number_divided = 0
    number_iteration = len(s) - (m - 1)
    for i in range(number_iteration):
        if sum(s[i:i+m]) == d:
            number_divided += 1
    return number_divided