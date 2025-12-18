"""
QUESTION:
Implement a function named `count_string_length` that takes a string as input and returns the length of the string. The function should use a for loop to iterate over each character in the string and count them. Do not use the built-in len() function or any other built-in function to count the length of the string.
"""

def count_string_length(input_string):
    """
    This function takes a string as input and returns the length of the string.
    It uses a for loop to iterate over each character in the string and count them.

    Args:
        input_string (str): The input string.

    Returns:
        int: The length of the input string.
    """
    count = 0
    for char in input_string:
        count += 1
    return count