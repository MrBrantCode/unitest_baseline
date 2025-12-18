"""
QUESTION:
Write a function `fibonacci_walks(N, MOD)` to calculate the total number of paths Alice can traverse from (0,0) to (N,N) in a grid where the distance between two lattice points corresponds to a Fibonacci number and both x and y coordinates are non-negative, modulo MOD. The Fibonacci numbers are generated up to the square root of twice the square of N. The function should use dynamic programming to optimize the solution and return the result modulo MOD.
"""

from math import sqrt

def fibonacci_walks(N, MOD):
    fib = [1, 1]
    while fib[-1] <= sqrt(2*N)**2:
        fib.append(fib[-1] + fib[-2])
    fib.pop()  
    pts = []
    for f in fib[1:]:
        for x in range(int(sqrt(f))+1):
            y = sqrt(f-x**2)
            if y == int(y):
                pts.append((x, int(y)))
    f = [[0]*(N+1) for _ in range(N+1)]
    f[0][0] = 1
    for x in range(N+1):
        for y in range(N+1):
            for dx, dy in pts:
                if x-dx >= 0 and y-dy >= 0:
                    f[x][y] += f[x-dx][y-dy]
                    f[x][y] %= MOD
    return f[N][N]