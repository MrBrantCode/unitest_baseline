"""
QUESTION:
Implement a recursive function `A(n)` that takes a positive integer `n` as input, subtracts 3 from it, and calls itself with the updated value if the result is non-negative. The function should terminate when `n` becomes negative.
"""

def A(n):
    """
    Recursive function that subtracts 3 from the input number n 
    and calls itself with the updated value if the result is non-negative.
    
    Args:
        n (int): A positive integer.

    Returns:
        None
    """
    # Base case: terminate recursion if n is negative
    if n < 0:
        return
    
    # Recursive case: subtract 3 from n and call A(n-3)
    A(n - 3)