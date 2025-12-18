"""
QUESTION:
Create a function `multiply_matrices` that takes two 2D arrays `mat1` and `mat2` of size n x n as input, where 1 ≤ n ≤ 10^3 and each element is an integer between -10^3 and 10^3. The function should return a new 2D array of size n x n representing the product of `mat1` and `mat2`. The solution must not use any built-in functions or libraries for matrix operations and should only use basic operations like addition, subtraction, and multiplication.
"""

def multiply_matrices(mat1, mat2):
    n = len(mat1)
    res = [[0]*n for _ in range(n)]  

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat1[i][k]*mat2[k][j]  

    return res