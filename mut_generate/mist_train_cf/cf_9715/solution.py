"""
QUESTION:
Create a function named `sum_even_odd` that takes an integer `n` as input and calculates the sum of all even numbers and the sum of all odd numbers between 1 and `n` (inclusive). The function should return the sum of even numbers and the sum of odd numbers. There are no restrictions on the programming language or approach used.
"""

def sum_even_odd(n):
    """
    Calculate the sum of even and odd numbers between 1 and n (inclusive).
    
    Args:
    n (int): The upper limit of the range.
    
    Returns:
    tuple: A tuple containing the sum of even numbers and the sum of odd numbers.
    """
    sum_even = sum(num for num in range(1, n+1) if num % 2 == 0)
    sum_odd = sum(num for num in range(1, n+1) if num % 2 != 0)
    
    return sum_even, sum_odd