"""
QUESTION:
Write a function `calculate_surface_area(grid: List[List[int]]) -> int` to calculate the total surface area of all the buildings in a city given a 2D grid representing a map of the city, where each cell contains a non-negative integer representing the height of the corresponding building. The surface area of each building is calculated as 2 * (1 + height) when there are no adjacent buildings, and the area of the shared face is the absolute difference in their heights if two adjacent buildings are of different heights.

The input `grid` is a 2D list of non-negative integers representing the heights of the buildings. The dimensions of the grid are N x N, where 1 <= N <= 50. The output should be an integer representing the total surface area of all the buildings in the city.
"""

from typing import List

def surface_area(grid: List[List[int]]) -> int:
    N = len(grid)
    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                continue
            height = grid[i][j]
            ans += 2
            for h in range(1, height + 1):
                adj = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
                for a, b in adj:
                    if a < 0 or a >= N or b < 0 or b >= N:
                        ans += h
                    else:
                        ans += max(0, h - grid[a][b])
    return ans