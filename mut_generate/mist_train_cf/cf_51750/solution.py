"""
QUESTION:
Estimate the upper bound for the value of f(N) in the recurrence relation f(2N + 1) = f(2N) = f(N) + log N, where N >= 1 and f(1) = 0.
"""

def entrance(n):
    """
    This function calculates the upper bound for the value of f(N) 
    in the recurrence relation f(2N + 1) = f(2N) = f(N) + log N.

    Args:
        n (int): The input number.

    Returns:
        float: The upper bound for the value of f(N).
    """
    import math
    if n == 1:
        return 0
    else:
        return math.log2(n) * math.log(n)