"""
QUESTION:
Write a function `numSpecial(mat)` that takes a binary matrix `mat` as input and returns the number of special positions in `mat`. A position `(i, j)` is considered special if `mat[i][j] == 1`, all other elements in row `i` and column `j` are `0`, and the sum of its row index `i` and column index `j` is an even number. The matrix `mat` has dimensions `rows x cols`, where `1 <= rows, cols <= 100` and `mat[i][j]` is either `0` or `1`.
"""

def numSpecial(mat):
    rows, cols = len(mat), len(mat[0])
    row_sums = [sum(row) for row in mat]
    col_sums = [sum(mat[i][j] for i in range(rows)) for j in range(cols)]
        
    return sum(
        mat[i][j] == 1 and row_sums[i] == col_sums[j] == 1 and (i + j) % 2 == 0
        for i in range(rows) 
        for j in range(cols)
    )