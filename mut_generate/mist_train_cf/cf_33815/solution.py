"""
QUESTION:
Implement the `factorial_recursive` function, which takes a non-negative integer `n` as input and returns its factorial using recursion. The function should not use loops and the input integer `n` will always be non-negative.
"""

def entance(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * entance(n - 1)