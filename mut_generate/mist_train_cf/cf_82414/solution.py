"""
QUESTION:
Create a function `fib(n, m)` that takes two integers as arguments: `n` and `m`, where `n` is the position of the Fibonacci number to be calculated and `m` is a positive integer used for modular calculation. The function should return the nth Fibonacci number modulo `m`. The function should be efficient to handle very large numbers.
"""

def fib(n, m):
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0

    def multiply(F, M, m):
        x = ((F[0][0] * M[0][0]) % m + (F[0][1] * M[1][0]) % m) % m
        y = ((F[0][0] * M[0][1]) % m + (F[0][1] * M[1][1]) % m) % m
        z = ((F[1][0] * M[0][0]) % m + (F[1][1] * M[1][0]) % m) % m
        w = ((F[1][0] * M[0][1]) % m + (F[1][1] * M[1][1]) % m) % m

        F[0][0] = x
        F[0][1] = y
        F[1][0] = z
        F[1][1] = w

    def power(F, n, m):
        M = [[1, 1],
             [1, 0]]
        for _ in range(2, n + 1):
            multiply(F, M, m)

    power(F, n - 1, m)
    return F[0][0]