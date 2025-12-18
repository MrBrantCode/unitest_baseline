"""
QUESTION:
Write a recursive function called `fibo(n)` that calculates the nth number in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should handle integers n greater than or equal to 0.
"""

def fibo(n): 
    """
    Calculates the nth number in the Fibonacci sequence.
    
    Args:
        n (int): The position of the number in the Fibonacci sequence.
    
    Returns:
        int: The nth number in the Fibonacci sequence.
    """
    if n <= 1: 
        return n 
    else: 
        return fibo(n-1) + fibo(n-2)