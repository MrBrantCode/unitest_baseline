"""
QUESTION:
Write a function named sum_of_products that calculates the sum of products of integers from 0 to n. The function should take an integer n as input and return the sum of products of integers from 0 to n, where each integer i from 0 to n is multiplied by all integers from 0 to n. The function should be optimized to eliminate the need for nested loops.
"""

def sum_of_products(n):
    """
    Calculate the sum of products of integers from 0 to n.

    Args:
    n (int): The input integer.

    Returns:
    int: The sum of products of integers from 0 to n.
    """
    return n * 100 + (n*(n+1))//2 * 100