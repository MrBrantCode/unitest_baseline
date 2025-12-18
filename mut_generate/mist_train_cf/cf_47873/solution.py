"""
QUESTION:
Create a function called `numSpecial` that takes a binary matrix `mat` as input where `1 <= mat.length <= 100` and `1 <= mat[i].length <= 100`. Return the number of special positions in `mat`, where a position `(i, j)` is special if `mat[i][j] == 1`, all other elements in row `i` and column `j` are `0`, and the sum of `i` and `j` is an even number.
"""

def numSpecial(mat):
    row_sums = list(map(sum, mat))
    col_sums = list(map(sum, zip(*mat)))
    special_count = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1 and (row_sums[i] == col_sums[j] == 1) and (i + j) % 2 == 0:
                special_count += 1
    return special_count