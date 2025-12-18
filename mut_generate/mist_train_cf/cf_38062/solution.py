"""
QUESTION:
Given a 2D grid of size N x N with cells labeled "W" or "B", write a function `count_good_rectangles` that returns the count of "good" rectangles, where a "good" rectangle is defined as a rectangle with sides parallel to the grid's axes and containing an equal number of "W" and "B" cells. The function takes the grid as input and should return an integer. Each cell is associated with a pair of coordinates (i, j), where 1 ≤ i, j ≤ N.
"""

from typing import List

def count_good_rectangles(grid: List[List[str]]) -> int:
    n = len(grid)
    prefix_sums = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix_sums[i][j] = prefix_sums[i-1][j] + prefix_sums[i][j-1] - prefix_sums[i-1][j-1] + (grid[i-1][j-1] == "W")

    count = 0
    for x1 in range(n):
        for x2 in range(x1, n):
            for y1 in range(n):
                for y2 in range(y1, n):
                    if (x2 - x1 + 1) * (y2 - y1 + 1) % 2 == 0:
                        w_count = prefix_sums[x2 + 1][y2 + 1] - prefix_sums[x1][y2 + 1] - prefix_sums[x2 + 1][y1] + prefix_sums[x1][y1]
                        b_count = (x2 - x1 + 1) * (y2 - y1 + 1) - w_count
                        if w_count == b_count:
                            count += 1
    return count