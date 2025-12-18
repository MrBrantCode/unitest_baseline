"""
QUESTION:
Given a triangle represented as a list of lists where each inner list represents a row of the triangle, implement the function `find_min_path(triangle)` that returns the minimum path sum from the top to the bottom of the triangle, moving only to adjacent numbers on the row below.
"""

def find_min_path(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for i in range(len(triangle[row])):
            triangle[row][i] += min(triangle[row + 1][i], triangle[row + 1][i + 1])
    return triangle[0][0]