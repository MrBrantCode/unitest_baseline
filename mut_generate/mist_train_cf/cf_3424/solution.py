"""
QUESTION:
Write a function `convert_string_to_unique_sorted_list` that takes a string of space-separated integers as input. The function should return a list of unique integers in descending order.
"""

def convert_string_to_unique_sorted_list(input_string):
    """
    This function takes a string of space-separated integers, removes duplicates, 
    and returns a list of unique integers in descending order.

    Args:
        input_string (str): A string of space-separated integers.

    Returns:
        list: A list of unique integers in descending order.
    """
    # Convert the string into a list of integers
    numbers = list(map(int, input_string.split()))
    
    # Remove duplicate values and sort the list in descending order
    return sorted(set(numbers), reverse=True)