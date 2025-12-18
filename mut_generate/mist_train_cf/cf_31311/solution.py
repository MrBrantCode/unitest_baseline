"""
QUESTION:
You are given a 2D terrain represented as a list of strings with '.' for open space and '#' for trees. Write a function `count_trees(terrain, hor, ver)` to calculate the number of trees encountered while traversing the terrain following a slope defined by horizontal movement `hor` and vertical movement `ver`. The traversal starts from the top-left position and wraps around to the left edge when reaching the right edge.
"""

def count_trees(terrain, hor, ver):
    tree_count = 0
    x = 0
    y = 0
    width = len(terrain[0])

    while y < len(terrain):
        if x >= width:
            x = x - width

        if terrain[y][x] == '#':
            tree_count += 1
        x += hor
        y += ver

    return tree_count