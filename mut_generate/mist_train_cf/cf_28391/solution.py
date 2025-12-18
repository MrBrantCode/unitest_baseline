"""
QUESTION:
Given a list of integers representing the heights of people standing in a queue, write a function `count_taller_pairs` that takes this list and returns the number of ways to choose two people such that the first person is taller than the second person. The function should take a list of integers `heights` as input and return the count of taller pairs as an integer.
"""

from typing import List

def count_taller_pairs(heights: List[int]) -> int:
    taller_pairs = 0
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            if heights[i] > heights[j]:
                taller_pairs += 1
    return taller_pairs