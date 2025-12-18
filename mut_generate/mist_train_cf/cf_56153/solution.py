"""
QUESTION:
Write a function `generate(numRows)` that generates the first numRows of Pascal's triangle. The function should return a 2D list where each inner list represents a row in the triangle.

The function should follow these restrictions:
- `1 <= numRows <= 30`
- Each number in the triangle is the sum of the two numbers directly above it.
- The first and last numbers of each row are always 1.

Write another function `validate(triangle)` that takes a 2D list representing a Pascal's triangle as input and returns `True` if it is a valid Pascal's triangle and `False` otherwise. A valid Pascal's triangle is one where each number (except the first and last numbers of each row) is the sum of the two numbers directly above it.
"""

def generate(numRows):
    triangle = [[1]*(i+1) for i in range(numRows)]
    for i in range(2, numRows):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

def validate(triangle):
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):  
            if triangle[i][j] != triangle[i - 1][j - 1] + triangle[i - 1][j]:
                return False  
    return True 