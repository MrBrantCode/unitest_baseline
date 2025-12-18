"""
QUESTION:
Write a function named `pascal_triangle(n)` that prints and returns the sum of all elements in a Pascal's triangle of `n` rows. The function should dynamically generate the triangle and handle the calculation of the sum of its elements. The function's return type should be an integer, and it should only use the minimum required space for the triangle.
"""

def pascal_triangle(n):
    triangle = [[0 for x in range(y+1)] for y in range(n)]
    sum = 0
    for line in range(0, n):
        for i in range(0, line + 1):
            if i == 0 or i == line:
                triangle[line][i] = 1
            else:
                triangle[line][i] = (triangle[line-1][i-1] + triangle[line-1][i])
            sum += triangle[line][i]
    return sum