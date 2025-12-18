"""
QUESTION:
Implement a function named `fibonacci(n, m)` that calculates the nth Fibonacci number modulo `m`. The function should handle large values of `n` and `m` efficiently. The input parameters are `n`, a non-negative integer representing the position of the Fibonacci number to be calculated, and `m`, a non-negative integer representing the modulo value. The function should return the result of the calculation.
"""

def fibonacci(n, m):
    memo = [0, 1] + [-1]*(n-1)

    def fib_memo(k, mod):
        if memo[k] != -1:
            return memo[k]
        if k <= 1 : 
            return k
        memo[k] = (fib_memo(k-1, mod) + fib_memo(k-2, mod)) % mod
        return memo[k]

    return fib_memo(n, m)