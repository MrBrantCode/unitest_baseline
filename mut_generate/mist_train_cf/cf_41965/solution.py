"""
QUESTION:
You are given a triangular array of integers where each number is directly below and to either side of the numbers in the row above. Write a function `findMaxPathSum` that takes the triangular array as input and returns the maximum path sum from the top to the bottom of the triangle. The maximum path sum is defined as the maximum total sum of integers in a path from the top to the bottom moving only to adjacent numbers on the row below. Function signature: `def findMaxPathSum(triangle: List[List[int]]) -> int`.
"""

from typing import List

def findMaxPathSum(triangle: List[List[int]]) -> int:
    n = len(triangle)
    
    # Start from the second last row and move upwards
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            # For each element, find the maximum sum path from that element to the bottom
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    # The top element will have the maximum path sum
    return triangle[0][0]