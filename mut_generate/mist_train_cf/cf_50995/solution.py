"""
QUESTION:
Implement a function `fibfib_sequence(n: int, a: int, b: int, c: int) -> int` that calculates the n-th element of a modified Fibonacci sequence using dynamic programming. The sequence is defined as: `fibfib(0) -> a`, `fibfib(1) -> b`, `fibfib(2) -> c`, and `fibfib(n) -> fibfib(n-1) + fibfib(n-2) + fibfib(n-3)` for `n > 2`.
"""

def fibfib_sequence(n: int, a: int, b: int, c: int) -> int:
    if n == 0: return a
    elif n == 1: return b
    elif n == 2: return c

    dp = [0] * (n + 1)
    dp[0] = a
    dp[1] = b
    dp[2] = c

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]