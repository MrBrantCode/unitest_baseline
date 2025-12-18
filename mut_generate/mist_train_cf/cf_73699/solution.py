"""
QUESTION:
Create a function `get_string_before_second_last_hyphen` that takes an input string and returns everything from the start of the input to the second from the last occurrence of '-' or a copy of the input if there are less than 2 occurrences of '-'.
"""

def get_string_before_second_last_hyphen(input_str):
    """
    This function takes an input string and returns everything from the start of the input to the second from the last occurrence of '-'.
    If there are less than 2 occurrences of '-', it returns a copy of the input.

    Args:
        input_str (str): The input string.

    Returns:
        str: Everything from the start of the input to the second from the last occurrence of '-' or a copy of the input.
    """
    if input_str.count('-') < 2:
        return input_str
    else:
        reversed_str = input_str[::-1]
        second_last_hyphen_index = reversed_str.find('-', reversed_str.find('-') + 1)
        desired_position = len(input_str) - second_last_hyphen_index
        return input_str[:desired_position]