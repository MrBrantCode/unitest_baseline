"""
QUESTION:
Implement the function `red_and_blue(red, blue)` that takes two arrays of integers as input and returns the maximum absolute difference between the sum of elements in the red array and the sum of elements in the blue array. The arrays red and blue may have different lengths and may contain both positive and negative integers.
"""

from typing import List

def red_and_blue(red: List[int], blue: List[int]) -> int:
    sum_red = sum(red)
    sum_blue = sum(blue)
    return abs(sum_red - sum_blue)