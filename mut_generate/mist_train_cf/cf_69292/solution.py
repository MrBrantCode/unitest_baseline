"""
QUESTION:
Create a function `generate_spiral(m, n)` that generates a multidimensional array of dimension m (rows) and n (columns) and populates it with monotonically increasing integers starting from 1, in spiral order. Then create another function `get_submatrix(matrix, i_start, i_end, j_start, j_end)` that extracts a sub-matrix from the generated matrix or any other valid matrix, based on the provided range of indices (i_start, i_end) for rows and (j_start, j_end) for columns. Ensure that the function handles edge cases where parameters are out of bounds or invalid.
"""

def generate_spiral(m, n):
    result = [[0]*n for _ in range(m)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for _ in range(m*n):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and result[nx][ny] == 0:
                result[nx][ny] = c
                x, y, c = nx, ny, c + 1
                break
            dx[i], dy[i] = -dy[i], dx[i]
    return result


def get_submatrix(matrix, i_start, i_end, j_start, j_end):
    if min(i_start, i_end, j_start, j_end) < 0 or len(matrix) <= i_end or len(matrix[0]) <= j_end:
        return 'Invalid indices'
    return [ row[j_start:j_end+1] for row in matrix[i_start:i_end+1]]