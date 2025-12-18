"""
QUESTION:
Write a function `minFlips(mat)` that takes a binary grid `mat` as input and returns the minimum number of flips required to transform it into a unit matrix. A unit matrix is a square grid with ones on the principal diagonal and zeros elsewhere. In a single move, a cell can be flipped along with its four adjacent cells (horizontally and vertically). However, cells on the periphery of the grid (first and last rows and columns) cannot be flipped. If it's impossible to transform the grid into a unit matrix, return -1. The grid size `n` is between 3 and 5, inclusive.
"""

def minFlips(mat):
    N = len(mat)
    unit_matrix = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    def flip(i, j):
        for x, y in [(i, j), (i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if 0 <= x < N and 0 <= y < N:
                mat[x][y] ^= 1
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1 or j == 0 or j == N-1:
                if mat[i][j] != unit_matrix[i][j]:
                    return -1
    res = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            if mat[i][j] != unit_matrix[i][j]:
                flip(i, j)
                res += 1
    return res