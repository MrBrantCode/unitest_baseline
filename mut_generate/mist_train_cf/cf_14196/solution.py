"""
QUESTION:
Create a function `sort_even_numbers` that takes an array of integers as input and returns a new array containing only the even numbers from the input array, sorted in ascending order. The input array must contain at least 10 elements.
"""

def sort_even_numbers(numbers):
    """
    This function takes an array of integers as input and returns a new array containing 
    only the even numbers from the input array, sorted in ascending order.
    
    Args:
        numbers (list): A list of integers with at least 10 elements.
    
    Returns:
        list: A new list containing only the even numbers from the input array, 
              sorted in ascending order.
    """
    return sorted([num for num in numbers if num % 2 == 0])