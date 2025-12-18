"""
QUESTION:
Write a function, get_even_numbers, that generates a list of all even numbers between two given numbers, inclusive, and returns the list. The function should take two integer arguments, start and end, where start is less than or equal to end.
"""

def get_even_numbers(start, end):
    """
    Generates a list of all even numbers between two given numbers, inclusive.
    
    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).
    
    Returns:
        list: A list of even numbers between start and end.
    """
    return [x for x in range(start, end + 1) if x % 2 == 0]