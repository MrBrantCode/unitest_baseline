"""
QUESTION:
Write a function `generate_pascals_triangle(numRows)` that generates the first `numRows` of Pascal's triangle. The function should take an integer `numRows` as input and return the result as a list of lists, where each sublist represents a row in the triangle. The function should construct each row by summing the adjacent elements from the previous row, with the first and last elements of each row always being 1.
"""

def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []
    triangle = [[1]]
    for i in range(1, numRows):
        prev_row = triangle[i - 1]
        new_row = [1]  
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  
        triangle.append(new_row)
    return triangle