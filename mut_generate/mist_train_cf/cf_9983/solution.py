"""
QUESTION:
Implement a function `tail_recursion_optimization` that demonstrates the difference between tail recursion and regular recursion in terms of memory usage.
"""

def tail_recursion_optimization(n, accumulator=0):
    """
    This function demonstrates tail recursion optimization by summing the numbers from 0 to n.
    
    Args:
    n (int): The upper limit of the sum.
    accumulator (int): The accumulated sum (default is 0).
    
    Returns:
    int: The sum of numbers from 0 to n.
    """
    if n == 0:
        return accumulator
    else:
        return tail_recursion_optimization(n - 1, accumulator + n)