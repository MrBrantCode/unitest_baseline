"""
QUESTION:
Given a triangle represented as a 2D list of integers, write a function max_total(triangle) that finds the maximum total from top to bottom by moving to adjacent numbers on the row below. The function should take the 2D list as input and return the maximum total.
"""

def max_total(triangle):
    """
    Find the maximum total from top to bottom in a triangle.
    """
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]