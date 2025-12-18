"""
QUESTION:
Implement a function `orderOfLargestPlusSign` that takes two inputs, `N` and `mines`, and returns the order of the largest axis-aligned plus sign composed of 1's within an NxN grid where each cell is filled with a 1, except for the cells specified in the `mines` list, which are filled with 0's. The function should have a time complexity of O(N^2). `N` will be an integer in the range [1, 500], and `mines` will have length at most 5000 with each mine being a list of two integers in the range [0, N-1].
"""

def orderOfLargestPlusSign(N, mines):
    grid = [[1]*N for _ in range(N)]
    left = [[1]*N for _ in range(N)]
    right = left.copy()
    up = left.copy()
    down = left.copy()

    for [i, j] in mines:
        grid[i][j] = 0
        left[i][j] = 0
        right[i][j] = 0
        up[i][j] = 0
        down[i][j] = 0

    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                if i>0: up[i][j] = min(up[i][j], up[i-1][j]+1)
                if j>0: left[i][j] = min(left[i][j], left[i][j-1]+1)

    maximum = 0
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if grid[i][j]:
                if i<N-1: down[i][j] = min(down[i][j], down[i+1][j]+1)
                if j<N-1: right[i][j] = min(right[i][j], right[i][j+1]+1)
                maximum = max(maximum, min(left[i][j], right[i][j], up[i][j], down[i][j]))
    return maximum