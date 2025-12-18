"""
QUESTION:
Create a function `find_even_numbers` that takes a list of integers as input and returns a list of even numbers from the input list.
"""

def find_even_numbers(numbers):
    """
    This function takes a list of integers as input and returns a list of even numbers from the input list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of even numbers from the input list.
    """
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:  
            even_numbers.append(num)
    return even_numbers