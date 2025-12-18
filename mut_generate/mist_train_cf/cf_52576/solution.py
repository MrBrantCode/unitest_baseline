"""
QUESTION:
Write a function named `fibfib(n)` that calculates the nth element of the FibFib series. The FibFib series has the following properties: fibfib(0) = 0, fibfib(1) = 0, fibfib(2) = 1, and fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3). The function should use dynamic programming and be efficient for n up to 10^4.
"""

def fibfib(n: int):
    """
    The FibFib series resembles the Fibonacci sequence with the following properties:
    fibfib(0) == 0, fibfib(1) == 0, fibfib(2) == 1, and fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Compose a function, utilizing dynamic programming, to effectively compute the n-th element of this series.
    """
    # Using memoization to store the previously computed values
    memo = {0: 0, 1: 0, 2: 1}

    if n in memo:
        return memo[n]
    memo[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    return memo[n]