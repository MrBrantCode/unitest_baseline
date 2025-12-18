"""
QUESTION:
Create a function called `remove_alphabets` that takes a string of alphanumeric characters as input and returns a string containing only the numeric characters. The input string can contain both uppercase and lowercase letters and any digit from 0 to 9.
"""

def remove_alphabets(s):
    """
    This function takes a string of alphanumeric characters as input and returns a string containing only the numeric characters.
    
    Parameters:
    s (str): The input string of alphanumeric characters.
    
    Returns:
    str: A string containing only the numeric characters from the input string.
    """
    return ''.join(filter(str.isdigit, s))