"""
QUESTION:
Write a function `numDistinctIslands2` that takes a 2D grid of 1s and 0s as input, and returns the number of distinct islands in the grid. Two islands are considered distinct if one is not a translation or rotation of the other. The grid is represented as a list of lists, where 1 represents land and 0 represents water.
"""

def numDistinctIslands2(grid):
    def dfs(i, j, direction, path):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1):
            return
        grid[i][j] = 0
        path.append(direction)
        dfs(i-1, j, 'u', path)
        dfs(i+1, j, 'd', path)
        dfs(i, j-1, 'l', path)
        dfs(i, j+1, 'r', path)
        path.append('e')

    def normalize(path):
        paths = [path, path[::-1], path.replace('u', '#').replace('d', 'u').replace('#', 'd'), 
                 path.replace('l', '#').replace('r', 'l').replace('#', 'r')]
        return min(paths)

    shapes = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                path = []
                dfs(i, j, 's', path)
                shape = normalize(''.join(path))
                shapes.add(shape)
    return len(shapes)