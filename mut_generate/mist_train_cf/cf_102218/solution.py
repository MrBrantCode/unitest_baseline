"""
QUESTION:
Write a function `increase_string` that takes a string as input and returns or prints the string with its characters reversed if the string is not empty. If the string is empty, return or print a message indicating that the string cannot be increased. The time complexity of the solution should be O(n), where n is the length of the original string.
"""

def increase_string(string):
    """
    Returns the input string with its characters reversed if the string is not empty.
    If the string is empty, returns a message indicating that the string cannot be increased.

    Args:
        string (str): The input string.

    Returns:
        str: The reversed string or an error message if the string is empty.
    """
    if string != "":
        return string[::-1]
    else:
        return "String cannot be increased."