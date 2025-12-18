"""
QUESTION:
Write a function `fibfib(n)` that efficiently calculates the n-th term of the FibFib number sequence, where fibfib(0) = 0, fibfib(1) = 0, fibfib(2) = 1, and fibfib(n) is the sum of fibfib(n-1), fibfib(n-2), and fibfib(n-3).
"""

def fibfib(n, cache = {}):
    """
    Calculate the n-th term of the FibFib number sequence.

    Args:
    n (int): Term number in the sequence.
    cache (dict, optional): Cache of previously calculated values. Defaults to {}.

    Returns:
    int: The n-th term of the FibFib sequence.
    """
    if n in (0, 1):
        return 0
    elif n == 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fibfib(n - 1, cache) + fibfib(n - 2, cache) + fibfib(n - 3, cache)
        return cache[n]