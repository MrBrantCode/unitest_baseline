"""
QUESTION:
Create a function named `get_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers from the original list. The function must use bitwise operations to determine if a number is even and cannot use any built-in functions or operators for checking if a number is even.
"""

def get_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the original list.
    
    Args:
    numbers (list): A list of integers.
    
    Returns:
    list: A list of even integers.
    """
    even_numbers = []
    
    for num in numbers:
        if num & 1 == 0:
            even_numbers.append(num)
    
    return even_numbers