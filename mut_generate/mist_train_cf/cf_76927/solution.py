"""
QUESTION:
Create a function called `split_string_to_characters` that takes a string as input and returns a list of alphabetic characters. The function should exclude numbers and special characters from the output list.
"""

def split_string_to_characters(s):
    """
    This function takes a string as input and returns a list of alphabetic characters.
    
    Parameters:
    s (str): The input string
    
    Returns:
    list: A list of alphabetic characters
    """
    return [char for char in s if char.isalpha()]