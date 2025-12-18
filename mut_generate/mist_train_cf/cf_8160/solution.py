"""
QUESTION:
Write a recursive function `increment(x, limit)` that increments the value of `x` by 1 and checks if it exceeds the specified `limit`. The function should return -1 if `x` exceeds the `limit`, otherwise it should continue to increment `x` until it reaches the `limit`.
"""

def entrance(x, limit):
    """
    Recursively increments the value of x by 1 and checks if it exceeds the specified limit.
    
    Args:
        x (int): The initial value.
        limit (int): The maximum allowed value.
    
    Returns:
        int: -1 if x exceeds the limit, otherwise the incremented value.
    """
    if x >= limit:
        return -1
    return entrance(x+1, limit)