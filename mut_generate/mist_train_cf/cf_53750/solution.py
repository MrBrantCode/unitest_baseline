"""
QUESTION:
Write a function called ascii_values that takes a string input and returns a list of ASCII values corresponding to each character in the string.
"""

def ascii_values(sentence):
    """
    This function takes a string input and returns a list of ASCII values corresponding to each character in the string.
    
    Parameters:
    sentence (str): The input string.
    
    Returns:
    list: A list of ASCII values.
    """
    return [ord(c) for c in sentence]