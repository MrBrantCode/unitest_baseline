"""
QUESTION:
Implement a function `spiralOrder(matrix)` that takes a 2D matrix of integers as input and returns a 1D list of integers representing the elements of the input matrix in a clockwise spiral order. The function should be able to handle matrices of any size, including empty matrices.
"""

def spiralOrder(matrix):
    if not matrix: return []
    R, C = len(matrix), len(matrix[0])
    visited = [[False] * C for _ in matrix]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ans = []
    r = c = di = 0
    for _ in range(R * C):
        ans.append(matrix[r][c])
        visited[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < R and 0 <= cc < C and not visited[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return ans