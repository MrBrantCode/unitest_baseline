"""
QUESTION:
Create a function `number_of_rectangles(m, n)` that calculates the total number of distinct rectangles that can be positioned within all grids of dimensions from 1x1 to mxn. The function should take two parameters, `m` and `n`, representing the dimensions of the grid. The function should return the total number of distinct rectangles that can be positioned within all the grids of dimensions from 1x1 to mxn.
"""

def number_of_rectangles(m, n):
    total_rectangles = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            total_rectangles += (i * (i + 1) * j * (j + 1)) // 4
    return total_rectangles