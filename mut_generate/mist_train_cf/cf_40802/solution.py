"""
QUESTION:
Implement the function `process_grid` that processes a given 2D grid of size `n x n` (1 <= n <= 100) containing only 0s and 1s. The function should populate three sets: `col_blacklist`, `major_blacklist`, and `minor_blacklist` based on the following rules:
- If a cell value is 0, add its column index to `col_blacklist`.
- If a cell value is 0 and the difference between its row and column indices is constant for all such cells, add this constant to `major_blacklist`.
- If a cell value is 0 and the sum of its row and column indices is constant for all such cells, add this constant to `minor_blacklist`.
The function should return the sum of the sizes of `col_blacklist`, `major_blacklist`, and `minor_blacklist`.
"""

from typing import List

def process_grid(grid: List[List[int]]) -> int:
    n = len(grid)
    col_blacklist = set()
    major_blacklist = set()
    minor_blacklist = set()

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                col_blacklist.add(j)
                major_blacklist.add(i - j)
                minor_blacklist.add(i + j)

    return len(col_blacklist) + len(major_blacklist) + len(minor_blacklist)