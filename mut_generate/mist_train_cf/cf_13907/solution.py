"""
QUESTION:
Write a function `sum_odd_numbers` that calculates the sum of odd numbers from 0 to `n` (inclusive) using a while loop. The function should take an integer `n` as input and return the sum of odd numbers.
"""

def sum_odd_numbers(n):
    """
    Calculate the sum of odd numbers from 0 to n (inclusive) using a while loop.
    
    Args:
    n (int): The upper limit for summing odd numbers.
    
    Returns:
    int: The sum of odd numbers from 0 to n.
    """
    total_sum = 0
    num = 1

    while num <= n:
        if num % 2 == 1:
            total_sum += num
        num += 2

    return total_sum