"""
QUESTION:
Compute the factorial of a large number `n` (up to 10,000) modulo some number `m` using a function called `factorial(n, m)`, where `n` and `m` are integers. The function should efficiently handle large numbers and avoid overflow issues. If `n` is greater than `m`, the function should return 0.
"""

def factorial(n, m):
    """
    Compute the factorial of a large number `n` (up to 10,000) modulo some number `m`.
    
    Args:
    n (int): The input number to compute the factorial.
    m (int): The modulo number.
    
    Returns:
    int: The factorial of `n` modulo `m`. If `n` is greater than `m`, returns 0.
    """
    if n > m:
        return 0
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % m
    return res