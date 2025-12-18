"""
QUESTION:
Implement the function `is_local_min(matrix, x, y)` where `matrix` is a 2D list of integers representing an elevation map, and `x` and `y` are the coordinates of a cell. The function should return `True` if the cell at `(x, y)` is a local minimum (lower in elevation than its neighboring cells) and `False` otherwise, considering the following rules:
- If the cell is on the edge of the matrix, it should only be compared to its valid neighbors.
- If the cell has valid neighbors, it should be compared to all of them, and it is considered a local minimum if it is lower in elevation than all of its neighbors.
"""

def entrance(matrix, x, y):
    n = len(matrix)
    m = len(matrix[0])

    def is_valid_cell(i, j):
        return 0 <= i < n and 0 <= j < m

    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    valid_neighbors = [(i, j) for i, j in neighbors if is_valid_cell(i, j)]

    for i, j in valid_neighbors:
        if matrix[x][y] >= matrix[i][j]:
            return False

    return True