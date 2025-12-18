"""
QUESTION:
Create a function called `inverse_string` that takes an input string and returns its inverse form, which is the string with its characters in reverse order. The function should only reverse the order of the characters, without modifying or removing any characters, spaces, or punctuation. The input string can contain any characters, including uppercase and lowercase letters, numbers, spaces, and special characters. The function should not use any built-in string reversal methods, but instead use a loop to iterate through the input string.
"""

def inverse_string(input_string):
    """
    Returns the inverse form of the input string.
    
    The inverse form is the string with its characters in reverse order.
    This function only reverses the order of the characters, without modifying or removing any characters, spaces, or punctuation.
    
    Parameters:
    input_string (str): The input string to be reversed.
    
    Returns:
    str: The inverse form of the input string.
    """
    inverse = ""
    for i in range(len(input_string)-1, -1, -1):
        inverse += input_string[i]
    return inverse