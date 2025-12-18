"""
QUESTION:
Implement a function `calculateTotalPrice(grid)` that takes a two-dimensional array of integers representing product prices as input and returns the total price of all products in the grid. The grid can have varying numbers of rows and columns, and each row can have a different number of elements.
"""

def calculateTotalPrice(grid):
    total_price = 0
    for row in grid:
        total_price += sum(row)
    return total_price