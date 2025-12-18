"""
QUESTION:
Create a function `reshape_mat(mat, r, c)` that takes a 2D list `mat` and two positive integers `r` and `c` as input, and returns a reshaped 2D list with `r` rows and `c` columns. The elements in the reshaped list should be populated from the original list in row-traversing order. If the reshaping operation is not possible due to the size of the original list, return the original list. The height and width of the input matrix are within the range [1, 100].
"""

def reshape_mat(mat, r, c):
    flat = sum(mat, [])
    if len(flat) != r*c:
        return mat
    tuples = zip(*([iter(flat)]*c))
    return map(list, tuples)