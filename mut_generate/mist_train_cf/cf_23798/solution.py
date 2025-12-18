"""
QUESTION:
Create a function `trailing_zeros(n)` that calculates the number of trailing zeros in the factorial of a given number `n`. The function should not take any additional parameters and should return an integer representing the count of trailing zeros. Note that the input number `n` is a non-negative integer.
"""

def trailing_zeros(n):
    """
    Calculate the number of trailing zeros in the factorial of a given number n.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        int: The count of trailing zeros.
    """
    count = 0
    i = 5
    while (n/i >= 1): 
        count += int(n/i) 
        i *= 5
    return count