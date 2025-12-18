"""
QUESTION:
Write a function named `multiply` that takes two n x n matrices `m1` and `m2` and their size `n` as input, and returns their product. The function should not assume any specific size for the matrices. The output should be a new 2D list representing the product matrix.
"""

def multiply(m1, m2, n):
    result = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]
    return result