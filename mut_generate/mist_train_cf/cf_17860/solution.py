"""
QUESTION:
Create a function `generate_pascals_triangle` that generates Pascal's triangle up to a given prime row number less than 100. The function should return a 2D list representing the triangle. The row number will be provided as an argument to the function. Additionally, the function should calculate and return the sum of all elements in the generated Pascal's triangle.
"""

def generate_pascals_triangle(n):
    """
    Generates Pascal's triangle up to a given prime row number less than 100 and 
    returns a 2D list representing the triangle along with the sum of all elements.

    Args:
    n (int): The row number of Pascal's triangle.

    Returns:
    list, int: A 2D list representing Pascal's triangle and the sum of all elements.
    """
    triangle = [[1 for _ in range(i+1)] for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    total_sum = sum(sum(row) for row in triangle)
    return triangle, total_sum