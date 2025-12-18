"""
QUESTION:
Write a function named `fibonacci` that calculates the Fibonacci number for a given integer `n`, where `n` can be extremely large (up to 10^18). The function should be able to handle such large numbers efficiently.
"""

def fibonacci(n):
    def multiply(F, M):
        x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
        y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
        z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
        w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

        F[0][0] = x
        F[0][1] = y
        F[1][0] = z
        F[1][1] = w

    def power(F, n):
        M = [[1, 1],
             [1, 0]]

        # n - 1 times multiply the matrix to {{1,0},{0,1}}
        for _ in range(2, n+1):
            multiply(F, M)

    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]