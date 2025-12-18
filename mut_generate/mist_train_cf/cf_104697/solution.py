"""
QUESTION:
Write a function `foo(A, n)` to calculate the time complexity of the given code as a function of n, considering the worst-case scenario. The function takes an array A and an integer n as input, and returns the sum of the first n elements in array A.
"""

def foo(A, n):
    """
    Calculate the sum of the first n elements in array A.
    
    Parameters:
    A (list): Input array.
    n (int): Number of elements to sum.
    
    Returns:
    int: Sum of the first n elements in array A.
    """
    return sum(A[:n])