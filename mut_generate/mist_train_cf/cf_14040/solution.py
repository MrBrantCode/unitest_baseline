"""
QUESTION:
Write a function named `find_path` that finds a path from a source point to a destination point in a given 2D array while avoiding obstacles represented by a value of 1. The function should return the path as a list of coordinates, or `None` if no valid path exists. The source and destination points are represented as lists of two integers. The function should not include any obstacles in the path.
"""

def find_path(array, source, destination):
    rows = len(array)
    cols = len(array[0])

    if source[0] < 0 or source[0] >= rows or source[1] < 0 or source[1] >= cols:
        return None
    if destination[0] < 0 or destination[0] >= rows or destination[1] < 0 or destination[1] >= cols:
        return None

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []

    def find_path_helper(current):
        if current == destination:
            path.append(current)
            return True

        x, y = current
        if x < 0 or x >= rows or y < 0 or y >= cols or array[x][y] == 1 or visited[x][y]:
            return False

        visited[x][y] = True
        path.append(current)

        if find_path_helper([x-1, y]) or find_path_helper([x+1, y]) or \
           find_path_helper([x, y-1]) or find_path_helper([x, y+1]):
            return True

        path.pop()

        return False

    if find_path_helper(source):
        return path
    else:
        return None