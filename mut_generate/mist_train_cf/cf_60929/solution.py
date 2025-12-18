"""
QUESTION:
Create a function named `segment_even_odd` that takes a list of integers as input and returns two lists: one containing even numbers and the other containing odd numbers. The function should not modify the original list.
"""

def segment_even_odd(numbers):
    """
    Segregate a list of integers into two lists: one containing even numbers and the other containing odd numbers.
    
    Args:
    numbers (list): A list of integers.
    
    Returns:
    tuple: Two lists, the first containing even numbers and the second containing odd numbers.
    """
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]
    return even_numbers, odd_numbers