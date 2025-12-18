"""
QUESTION:
Create a function named `matrix_add` that takes two n x n matrices `mat1` and `mat2` as input, where 0 < n < 101. The function should return the sum of the two matrices based on the following rules: 
- If both numbers are even, multiply them before adding them to the resulting matrix.
- If both numbers are odd, add them together and subtract 3 before adding to the resulting matrix.
- If the numbers are different, simply add them together before adding to the resulting matrix.
"""

def matrix_add(mat1, mat2):
    n = len(mat1)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat1[i][j] % 2 == 0 and mat2[i][j] % 2 == 0:
                result[i][j] = mat1[i][j] * mat2[i][j]
            elif mat1[i][j] % 2 != 0 and mat2[i][j] % 2 != 0:
                result[i][j] = mat1[i][j] + mat2[i][j] - 3
            else:
                result[i][j] = mat1[i][j] + mat2[i][j]
    return result