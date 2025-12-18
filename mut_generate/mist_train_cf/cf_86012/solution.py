"""
QUESTION:
Create a Pascal's triangle generation function `generate_pascal_triangle(n)` that generates a Pascal's triangle for a given number of rows 'n'. The generated triangle should be a 2D list where the `i`-th row contains `i` elements. Also, create a display function `display_pascal_triangle(triangle, inverted=False)` that takes the generated triangle and displays it in both normal and inverted orientations. The function should indent each row with spaces to make it appear as a triangle. The inverted option should be triggered when `inverted=True`.
"""

def generate_pascal_triangle(n):
    triangle = [[1]*i for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

def display_pascal_triangle(triangle, inverted=False):
    n = len(triangle)
    if inverted:
        triangle = triangle[::-1]
    for i in range(n):
        print(' '*(n-i-1), end='')
        for j in range(len(triangle[i])):
            print(triangle[i][j], ' ', end='')
        print()