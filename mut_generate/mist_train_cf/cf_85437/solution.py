"""
QUESTION:
Given a 2D grid of 0's, 1's, and 2's where 1's represent land, 0's represent water, and 2's represent bridges that connect islands, write a function `numDistinctIslands(grid)` to count the number of distinct islands. Two islands are considered distinct if one cannot be translated to equal the other. The function should take a 2D grid as input and return an integer representing the number of distinct islands. The length of each dimension in the grid does not exceed 50.
"""

def numDistinctIslands(grid):
    seen = set()
    def explore(r, c, direction = 0):
        if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                grid[r][c] not in (0, '#') and (r, c) not in seen):
            seen.add((r, c))
            shape.append(direction)
            explore(r+1, c, 1)
            explore(r-1, c, 2)
            explore(r, c+1, 3)
            explore(r, c-1, 4)
            shape.append(0)

    shapes = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            shape = []
            if grid[r][c] == 1 and (r, c) not in seen:
                explore(r, c)
                shapes.add(tuple(shape))

    return len(shapes)