"""
QUESTION:
Create a function named `zigzag` that takes two parameters, `m` and `n`, representing the dimensions of a 2D array. Populate the array with numbers ranging from 1 to `m*n` in a zig-zag pattern. The pattern should start from the top left corner, moving right, then down, then left, and then up, repeating this process until all cells are filled. The function should return the populated 2D array.
"""

def zigzag(m, n):
    res = [[0] * n for _ in range(m)]
    i, j, pos, size = 0, 0, 1, m * n

    while pos <= size:
        # move to right
        while j < n and res[i][j] == 0:
            res[i][j] = pos
            pos += 1
            j += 1
        j -= 1
        i += 1 
        # move downwards
        while i < m and res[i][j] == 0:
            res[i][j] = pos
            pos += 1
            i += 1
        i -= 1
        j -= 1
        # move to left
        while j >= 0 and res[i][j] == 0:
            res[i][j] = pos
            pos += 1
            j -= 1
        j += 1
        i -= 1
        # move upwards
        while i >= 0 and res[i][j] == 0:
            res[i][j] = pos
            pos += 1
            i -= 1
        i += 1
        j += 1
    return res