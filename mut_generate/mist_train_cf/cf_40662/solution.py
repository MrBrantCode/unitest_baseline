"""
QUESTION:
Write a function `trapped_water(mesh)` that takes a 2D grid of non-negative integers representing terrain heights as input and returns the total amount of water that can be trapped within the mesh, assuming water can only be trapped if it forms a basin between higher terrain and the input mesh has at least 3x3 dimensions.
"""

from typing import List

def trapped_water(mesh: List[List[int]]) -> int:
    rows, cols = len(mesh), len(mesh[0])
    total_water = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            left_max = max(mesh[i][:j])
            right_max = max(mesh[i][j+1:])
            top_max = max(mesh[k][j] for k in range(i))
            bottom_max = max(mesh[k][j] for k in range(i+1, rows))

            current_height = mesh[i][j]
            water_level = min(left_max, right_max, top_max, bottom_max)

            if water_level > current_height:
                total_water += water_level - current_height

    return total_water