"""
QUESTION:
Write a function `pascal_triangle(n)` to generate a Pascal's triangle with `n` rows, where each number is the sum of the nearest two numbers in the line above. The function should optimize performance by reducing time and space complexity. The function should take an integer `n` as input and print the generated Pascal's triangle.
"""

def generate_pascal_triangle(n):
    # Creating a 2D list of n rows
    triangle = [[0 for _ in range(i+1)] for i in range(n)]

    # Iterate through every line 
    for line in range(n):
 
        # First and last values in every row are 1
        triangle[line][0] = triangle[line][line] = 1
 
        # Other values are the sum of the above two
        for i in range(1, line):
            triangle[line][i] = triangle[line-1][i-1] + triangle[line-1][i]

    return triangle