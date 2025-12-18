"""
QUESTION:
Given a 2D array representing a triangle of numbers, where each number can only be reached from the two numbers directly above it, write a function `maxTotal(triangle)` that returns the maximum total from top to bottom. The function takes in a 2D array `triangle` as input and returns an integer representing the maximum total. The input 2D array is guaranteed to be non-empty, and each inner list is guaranteed to have one more element than the previous list. The function should return the maximum sum of the numbers from top to bottom, with the restriction that each step can only move to adjacent numbers on the row below.
"""

from typing import List

def min_stone_sum(triangle: List[List[int]]) -> int:
    n = len(triangle)
    
    # Start from the second bottom row and work upwards
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            # For each position, choose the maximum adjacent number from the row below and add it to the current number
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    return triangle[0][0]