"""
QUESTION:
Write a function `processOperations(initialGrid, operations)` that takes a 3x3 grid represented as a 2D array and a list of operations as strings. The function should apply each operation to the grid and return the final state of the grid. The operations can either remove a letter at a specific position (i, j) or add a new letter at a specific position (i, j). Positions are 1-indexed. The function should not modify the initial grid directly, but instead create a copy to apply the operations.

The input is a 3x3 2D array of strings representing the initial grid and a list of strings representing the operations to be performed. The output is a 3x3 2D array of strings representing the final state of the grid after applying all the operations.
"""

from typing import List

def processOperations(initialGrid: List[List[str]], operations: List[str]) -> List[List[str]]:
    grid = [row[:] for row in initialGrid]  

    for operation in operations:
        if "removed" in operation:
            pos = operation.split(" removed at position ")[1]
            i, j = map(int, pos.strip("()").split(", "))
            grid[i-1][j-1] = ''  
        elif "added" in operation:
            letter, pos = operation.split(" added at position ")[0], operation.split(" added at position ")[1]
            i, j = map(int, pos.strip("()").split(", "))
            grid[i-1][j-1] = letter  

    return grid