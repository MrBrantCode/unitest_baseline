"""
QUESTION:
Given a list of integers representing people's heights, find the height of the person who is neither the tallest nor the shortest. The list will contain at least three elements. 

Write a function `find_middle_height` that takes a list of integers as input and returns the height of the middle person. The function should return the smaller height if there are two or more middle people.
"""

from typing import List

def find_middle_height(heights: List[int]) -> int:
    sorted_heights = sorted(heights)
    return sorted_heights[1]  # Return the second smallest height, which is the middle height