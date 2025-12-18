"""
QUESTION:
Write a function `find_basins` that takes a 2D list `topographic_map` as input and returns two lists: `basin_sizes` and `num_basins`. `topographic_map` represents a topographic map where each cell contains an integer representing the height of the land at that point. A point is considered a basin if it is surrounded by higher or equal points in all cardinal directions. 

- `basin_sizes` should contain the sizes of all the basins in the map, sorted in ascending order.
- `num_basins` should contain the number of basins in the map.

The input `topographic_map` is a 2D list of integers where each element `topographic_map[i][j]` represents the height of the land at position `(i, j)`. The dimensions of the map are at most 1000x1000.
"""

from typing import List, Tuple

def find_basins(topographic_map: List[List[int]]) -> Tuple[List[int], int]:
    def is_basin(i, j, height):
        return all(
            topographic_map[ni][nj] >= height
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            if 0 <= ni < len(topographic_map) and 0 <= nj < len(topographic_map[0])
        )

    def explore_basin(i, j, height, visited):
        if 0 <= i < len(topographic_map) and 0 <= j < len(topographic_map[0]) and not visited[i][j] and topographic_map[i][j] <= height:
            visited[i][j] = True
            return 1 + sum(explore_basin(ni, nj, height, visited) for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
        return 0

    visited = [[False for _ in range(len(topographic_map[0]))] for _ in range(len(topographic_map))]
    basin_sizes = []
    num_basins = 0

    for i in range(len(topographic_map)):
        for j in range(len(topographic_map[0])):
            if not visited[i][j] and is_basin(i, j, topographic_map[i][j]):
                basin_size = explore_basin(i, j, topographic_map[i][j], visited)
                basin_sizes.append(basin_size)
                num_basins += 1

    return sorted(basin_sizes), num_basins