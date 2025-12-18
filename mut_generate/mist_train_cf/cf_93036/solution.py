"""
QUESTION:
Generate a function `pascal_triangle` that takes a positive integer `n` as input, representing the number of rows in a Pascal Triangle. The function should return a list of lists, where each sublist represents a row in the Pascal Triangle. The Pascal Triangle is a triangular array of binomial coefficients where each number is the sum of the two numbers directly above it, and the first and last numbers in each row are always 1.
"""

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i+1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle