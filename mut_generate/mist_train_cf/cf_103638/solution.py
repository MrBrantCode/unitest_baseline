"""
QUESTION:
Write a function called sum_of_powers that calculates the sum of all powers of 2 up to 2^n. The function should take an integer n as input and return the sum. The input n is a non-negative integer.
"""

def sum_of_powers(n):
    """
    Calculates the sum of all powers of 2 up to 2^n.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        int: The sum of all powers of 2 up to 2^n.
    """
    total = 0
    for i in range(n + 1):
        total += 2 ** i
    return total