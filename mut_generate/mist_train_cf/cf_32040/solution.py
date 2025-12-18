"""
QUESTION:
Write a function `find_special_cell(input: List[List[int]])` that takes a 2D array `input` of integers as input and returns `True` if there exists a cell that is greater than or equal to all elements in its row and less than or equal to all elements in its column, and `False` otherwise.
"""

from typing import List

def entrance(input: List[List[int]]) -> bool:
    for i in range(len(input)):
        for j in range(len(input[0])):
            cur = input[i][j]
            if all(cur >= input[i][n] for n in range(len(input[i]))) and all(cur <= input[n][j] for n in range(len(input))):
                return True
    return False