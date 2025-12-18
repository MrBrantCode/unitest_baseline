"""
QUESTION:
Implement the function `filter_even_numbers` to isolate integers from a given list that are evenly divisible by 2. The function should take a list of integers as input and return a list of even integers. The function should not include any input validation or error checking.
"""

def filter_even_numbers(data):
    """
    This function filters out even numbers from a given list.
    
    Args:
    data (list): A list of integers.
    
    Returns:
    list: A list of even integers.
    """
    return [n for n in data if n % 2 == 0]