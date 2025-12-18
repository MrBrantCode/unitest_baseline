"""
QUESTION:
Write a function `fibfib` that takes an integer `n` as input and returns the `n`-th term of the FibFib series, where `fibfib(0) = 0`, `fibfib(1) = 0`, `fibfib(2) = 1`, and `fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)` for `n > 2`. Implement the function using dynamic programming to optimize time complexity.
"""

def fibfib(n):
    """
    Returns the n-th term of the FibFib series using dynamic programming.

    Args:
    n (int): The term number in the FibFib series.

    Returns:
    int: The n-th term of the FibFib series.
    """
    result = [0, 0, 1]
    
    if n < 3:
        return result[n]
    
    for i in range(3, n + 1):
        result.append(result[i-1] + result[i-2] + result[i-3])
    
    return result[n]