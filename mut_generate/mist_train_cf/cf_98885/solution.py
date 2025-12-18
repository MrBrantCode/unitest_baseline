"""
QUESTION:
Define a Python function named "sum_between_numbers" that takes two integers, m and n, as input and returns the sum of all the numbers between them (inclusive). The function should use a loop to calculate the sum. The function should also include a docstring explaining what the function does and the input/output parameters. The function should work for any two integers, regardless of order, and should handle negative numbers. The function should return an integer value representing the sum of all numbers between m and n (inclusive).
"""

def sum_between_numbers(m, n):
    """
    This function takes two integers, m and n, and returns the sum of all the numbers between them (inclusive).
    
    Args:
    m (int): The first integer
    n (int): The second integer
    
    Returns:
    int: The sum of all the numbers between m and n (inclusive)
    """
    if m > n:
        m, n = n, m
    total_sum = 0
    for i in range(m, n+1):
        total_sum += i
    return total_sum