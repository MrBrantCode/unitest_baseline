"""
QUESTION:
Write a function `generate_pascal_triangle(n)` that generates a Pascal's Triangle of `n` rows. The function should return a list of lists, where each sublist represents a row in the triangle. The function should not use any built-in Python library functions. The first and last element of each row should be 1, and each other element should be the sum of the two elements directly above it.
"""

def generate_pascal_triangle(n):
    pascal_triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j in (0, i): 
                row.append(1)
            else:
                row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]) 
        pascal_triangle.append(row)
    return pascal_triangle