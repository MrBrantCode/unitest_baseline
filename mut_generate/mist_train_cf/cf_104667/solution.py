"""
QUESTION:
Write a function named `sort_descending` that takes a list of integers as input, removes all numbers that are divisible by 3, and returns the remaining numbers in descending order.
"""

def sort_descending(numbers_list):
    """
    This function takes a list of integers, removes numbers divisible by 3, 
    and returns the remaining numbers in descending order.
    
    Args:
        numbers_list (list): A list of integers.
    
    Returns:
        list: The list of integers with numbers divisible by 3 removed, 
              sorted in descending order.
    """
    # remove numbers divisible by 3 and sort the remaining numbers in descending order
    return sorted([num for num in numbers_list if num % 3 != 0], reverse=True)