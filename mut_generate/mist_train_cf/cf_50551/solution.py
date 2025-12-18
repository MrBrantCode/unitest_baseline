"""
QUESTION:
Function: `bfs(matrix, src, dest)`

Write a function that checks if a path exists between two points in a given binary matrix and returns the shortest distance if the path exists. The matrix represents a bidimensional grid with n horizontal divisions and m vertical partitions, where 0 indicates a free path and 1 represents an obstacle. The function should take as input a 2D list `matrix`, the source position `src` as a tuple (x, y), and the destination position `dest` as a tuple (x, y).

Restrictions:
- The matrix is a 2D list of binary integers (0s and 1s).
- The source and destination positions are valid indices within the matrix.
- The function should return the shortest distance if a path exists, and infinity if no path exists.
- The function should have an optimized time complexity for large matrices.
"""

from collections import deque

def bfs(matrix, src, dest):
    n, m = len(matrix), len(matrix[0])
    
    row_num = [-1, 0, 0, 1]
    col_num = [0, -1, 1, 0]
    
    visited = [[False for _ in range(m)] for __ in range(n)]
    
    q = deque()
    q.append((src, 0))  # path distance from the source to src is 0
    
    while q:
        (x, y), dist = q.popleft()
        if (x, y) == dest:
            return dist  # if destination is reached, return distance

        # visit all neighboring cells
        for i in range(4):
            x_row, y_col = x + row_num[i], y + col_num[i]
            if (0 <= x_row < n) and (0 <= y_col < m) and (matrix[x_row][y_col] == 0) and (not visited[x_row][y_col]):
                visited[x_row][y_col] = True
                q.append(((x_row, y_col), dist + 1))
    return float("inf")  # if destination can not be reached, return infinity