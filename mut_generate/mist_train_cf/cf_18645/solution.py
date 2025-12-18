"""
QUESTION:
Create a function called `convert_strings_to_numbers` that takes an array of strings as input. The function should convert each string to a number, filter out non-positive integers, remove duplicates, and return the numbers in ascending order.
"""

def convert_strings_to_numbers(array):
    """
    This function takes an array of strings, converts each string to a number, 
    filters out non-positive integers, removes duplicates, and returns the numbers in ascending order.

    Parameters:
    array (list): A list of strings representing numbers

    Returns:
    list: A list of unique positive integers in ascending order
    """
    result = [int(string) for string in array if int(string) > 0]
    return sorted(set(result))