"""
QUESTION:
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:


Input: 4
Output: 2


Example 2:


Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

def compute_integer_sqrt(x: int) -> int:
    """
    Compute and return the integer part of the square root of x.

    Parameters:
    x (int): The non-negative integer for which to compute the square root.

    Returns:
    int: The integer part of the square root of x.
    """
    return int(x ** 0.5)