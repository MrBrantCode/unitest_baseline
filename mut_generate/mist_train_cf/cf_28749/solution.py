"""
QUESTION:
Implement the function `calculate_neighborhood_sum(grid, row, col)` to calculate the sum of the values in the 3x3 neighborhood cells of a given cell in a 2D grid. The function takes a 2D list `grid` and the coordinates `row` and `col` of the cell as input, and returns the sum of the values of the neighborhood cells. The neighborhood cells are defined as the cells immediately surrounding the given cell in a 3x3 grid pattern, and the sum should be calculated for all cells within the grid boundaries.
"""

def calculate_neighborhood_sum(grid, row, col):
    total_sum = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                total_sum += grid[i][j]
    return total_sum