"""
QUESTION:
Write a function called `extract_last_four` that takes a string as input. The function should extract the last four characters from the input string and return them in reverse order. If the input string has less than four characters, the function should return an empty string.
"""

def extract_last_four(input_str):
    """
    Extracts the last four characters from the input string and returns them in reverse order.
    
    If the input string has less than four characters, an empty string is returned.

    Args:
        input_str (str): The input string.

    Returns:
        str: The last four characters in reverse order.
    """
    last_four = ""
    if len(input_str) >= 4:
        last_four = input_str[-4:]
    return last_four[::-1]