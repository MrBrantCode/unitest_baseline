"""
QUESTION:
Write a function `generate(numRows: int)` that generates Pascal's Triangle up to the nth row and returns it as a list of lists of integers. The function should handle erroneous inputs gracefully without crashing, including cases where `numRows` is less than 1. If `numRows` is invalid, the function should print an error message and return an empty list. 

The function should also be able to handle user input errors, where the input is not a positive integer, and prompt the user to enter a valid input. The function should continue to prompt the user for input until a valid positive integer is entered.
"""

from typing import List

def generate(numRows: int) -> List[List[int]]:
    if numRows < 1:
        print("Error: The number of rows should be more than 0.")
        return []
    result = [[1]]
    for i in range(1, numRows):
        result.append([1] + [result[-1][j] + result[-1][j + 1] for j in range(i - 1)] + [1])
    return result