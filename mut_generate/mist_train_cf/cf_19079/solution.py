"""
QUESTION:
Write a function called `extract_last_four` that takes a string as input. The input string must contain at least one uppercase letter and one special character. The function should extract the last four characters from the string, reverse their order, and return them in lowercase. If the string has less than four characters, the function should return the reversed string in lowercase.
"""

def extract_last_four(text):
    """
    Extract the last four characters from the given text string, 
    reverse their order, and return them in lowercase.

    If the string has less than four characters, return the reversed string in lowercase.

    Parameters:
    text (str): The input string.

    Returns:
    str: The reversed last four characters in lowercase.
    """
    
    # Extract the last four characters or the entire string if it's shorter
    last_four = text[-4:]

    # Reverse the order of the last four characters and convert to lowercase
    return last_four[::-1].lower()