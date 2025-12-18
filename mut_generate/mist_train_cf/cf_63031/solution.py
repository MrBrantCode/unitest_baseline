"""
QUESTION:
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E', or empty '0', and a blast radius r, write a function maxKills(grid, r) that returns the maximum enemies you can kill using one bomb. The bomb can only be placed in an empty cell and kills all enemies in the same row and column from the planted point until it hits a wall. It also kills all enemies within its blast radius of r cells in all four directions (up, down, left, right). The bomb does not destroy walls and its blast radius stops expanding when it hits a wall.

Constraints: 1 <= m, n <= 500, grid[i][j] is either 'W', 'E', or '0', and 1 <= r <= min(m, n).
"""

def maxKills(grid, r):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    rowHits, colHits = [0]*cols, [[0]*cols for _ in range(rows)]
    maxKills = 0
    for row in range(rows):
        for col in range(cols):
            if col == 0 or grid[row][col-1] == 'W':
                rowHits[col] = 0
                n = col
                while n < cols and grid[row][n] != 'W':
                    if grid[row][n] == 'E':
                        rowHits[col] += 1
                    n += 1
            colHits[row][col] = rowHits[col] if row == 0 or grid[row-1][col] == 'W' else colHits[row-1][col]
            if grid[row][col] == '0':
                bombKills = rowHits[col] + colHits[row][col]
                if row - r >= 0:
                    bombKills -= colHits[row-r][col]
                if col - r >= 0:
                    bombKills -= rowHits[col-r]
                maxKills = max(maxKills, bombKills)
    return maxKills