"""
QUESTION:
Implement a recursive function sum_digits(n) to calculate the sum of the digits of a given positive integer n. The function should recursively break down the number into individual digits and return their sum. Provide the time complexity of this recursive function.
"""

def sum_digits(n):
    """
    Recursively calculates the sum of the digits of a given positive integer n.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        int: The sum of the digits of n.
    """
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)