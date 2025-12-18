"""
QUESTION:
Compute the total number of unique islands in a given grid, where an island is defined as a cluster of 1's linked in a 4-directional manner and islands connected by 2's (bridges) are considered a single island. Two islands are considered identical only if one can be translated (without rotation or reflection) to match the other. The grid is a non-empty 2D matrix composed of 0's, 1's, and 2's, where 0's denote water, 1's denote land, and 2's denote bridges. The length of each dimension in the grid does not exceed 50. Implement a function `numDistinctIslands` that takes a 2D grid as input and returns the number of unique islands.
"""

def numDistinctIslands(grid):
    seen = set()
    def explore(r, c, row, col, shape):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] not in ('0', '2') and (r, c) not in seen:
            seen.add((r, c))
            shape.add((r - row, c - col))  
            explore(r+1, c, row, col, shape)
            explore(r-1, c, row, col, shape)
            explore(r, c+1, row, col, shape)
            explore(r, c-1, row, col, shape)

    shapes = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] not in ('0', '2') and (r, c) not in seen:
                shape = set()
                explore(r, c, r, c, shape)
                if shape:
                    shapes.add(frozenset(shape))

    return len(shapes)