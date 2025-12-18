"""
QUESTION:
Write a function `fibfib(n: int)` to calculate the nth term of the FibFib sequence, which is defined as:
- fibfib(0) == 0
- fibfib(1) == 0
- fibfib(2) == 1
- fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n > 2
- fibfib(n) == fibfib(n+3) - fibfib(n+2) - fibfib(n+1) for n < 0
Use dynamic programming and memoization to optimize the function.
"""

def fibfib(n: int):
    """
    Calculate the nth term of the FibFib sequence.

    The FibFib sequence is defined as:
    - fibfib(0) == 0
    - fibfib(1) == 0
    - fibfib(2) == 1
    - fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n > 2
    - fibfib(n) == fibfib(n+3) - fibfib(n+2) - fibfib(n+1) for n < 0

    This function uses dynamic programming and memoization to optimize the calculation.

    Args:
        n (int): The term number in the FibFib sequence.

    Returns:
        int: The nth term of the FibFib sequence.
    """
    memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 0
    elif n == 2:
        memo[n] = 1
    elif n > 2:
        memo[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    elif n < 0:
        memo[n] = fibfib(n+3) - fibfib(n+2) - fibfib(n+1)
    return memo[n]