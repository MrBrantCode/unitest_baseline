"""
QUESTION:
Create a function named `sum_even_numbers` that takes an integer `n` as input and returns the sum of all even numbers from 1 to `n` (inclusive). The function should use a loop structure to calculate the sum.
"""

def sum_even_numbers(n):
    """
    Calculate the sum of all even numbers from 1 to n (inclusive).
    
    Args:
    n (int): The upper limit of the range of numbers.
    
    Returns:
    int: The sum of all even numbers in the range.
    """
    total_sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total_sum += i
    return total_sum