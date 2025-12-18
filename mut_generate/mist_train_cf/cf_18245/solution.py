"""
QUESTION:
Create a function called `convert_string_to_unique_sorted_list` that takes a string of space-separated integers as input, converts the string into a list of unique integers, and returns the list in ascending order. The function should not take any other arguments besides the input string.
"""

def convert_string_to_unique_sorted_list(input_string):
    """
    Converts a string of space-separated integers into a list of unique integers and returns the list in ascending order.

    Args:
        input_string (str): A string of space-separated integers.

    Returns:
        list: A list of unique integers in ascending order.
    """
    numbers = list(set(map(int, input_string.split())))
    numbers.sort()
    return numbers