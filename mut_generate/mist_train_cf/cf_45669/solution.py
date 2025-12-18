"""
QUESTION:
Given a binary matrix `mat` of size `rows x cols`, where each element is either `0` or `1`, write a function `numSpecial(mat)` to return the number of special positions in `mat`. A position `(i, j)` is considered special if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0`, and the sum of `i` and `j` is even. The constraints are: `1 <= rows, cols <= 100` and `mat[i][j]` is either `0` or `1`.
"""

def numSpecial(mat):
    rows, cols = len(mat), len(mat[0])
    row_sums = [0]*rows
    col_sums = [0]*cols

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                row_sums[i] += 1
                col_sums[j] += 1

    res = 0
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1 and (i+j)%2 == 0:
                res += 1
    return res