"""
QUESTION:
Write a function `identify_walls(width, height, non_walls)` that takes in the width and height of a grid and a set of non-wall cells `non_walls`. The function should return a set containing the cells that are walls based on the grid and the provided set.
"""

def identify_walls(width, height, non_walls):
    walls = set()
    for x in range(width):
        for y in range(height):
            if (x, y) not in non_walls:
                walls.add((x, y))
    return walls