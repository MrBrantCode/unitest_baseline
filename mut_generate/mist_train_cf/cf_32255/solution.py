"""
QUESTION:
Write a function `count_trees` that takes a 2D grid of characters representing a field, where each cell is either a tree ('#') or open space ('.'), and two integers representing the horizontal and vertical slopes. The function should return the number of trees encountered while moving through the field from the top-left corner following the given slope. The horizontal slope represents the number of steps to move right in each iteration, and the vertical slope represents the number of steps to move down in each iteration. The function should handle cases where the horizontal slope exceeds the width of the field by assuming the field repeats to the right.
"""

from typing import List

def count_trees(field: List[List[str]], right_slope: int, down_slope: int) -> int:
    rows, cols = len(field), len(field[0])
    tree_count = 0
    x, y = 0, 0  

    while y < rows:
        if field[y][x % cols] == '#':
            tree_count += 1
        x += right_slope
        y += down_slope

    return tree_count