"""
QUESTION:
Create a function `pascal_triangle(n)` that generates a Pascal Triangle with n rows, where each number in the triangle is the sum of the two numbers directly above it, and the first and last numbers in each row are always 1. The function should return a list of lists representing the triangle. The input n is a positive integer.
"""

def pascal_triangle(n):
    """
    Generates a Pascal Triangle with n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing the Pascal Triangle.
    """
    triangle = []
    for i in range(n):
        row = [1] * (i+1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle