"""
QUESTION:
Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, write a function `countNegatives(grid)` that returns the number of negative numbers in `grid` and the index of the row that contains the maximum number of negative numbers. If there are multiple rows with the same maximum number of negative numbers, return the smallest index. If there are no negative numbers in the matrix, return the total count of negative numbers and `-1` for the row index.

Constraints: `m == grid.length`, `n == grid[i].length`, `1 <= m, n <= 100`, and `-100 <= grid[i][j] <= 100`.
"""

def entrance(grid):
    count = 0
    max_row = float('inf')
    max_count = 0
    for i in range(len(grid)):
        row_count = 0
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                count += 1
                row_count += 1
        if row_count > max_count:
            max_row = i
            max_count = row_count
        elif row_count == max_count:
            max_row = min(max_row, i)
    return (count, -1 if max_row == float('inf') else max_row)