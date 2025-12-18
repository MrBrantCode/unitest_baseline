"""
QUESTION:
Create a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome and `False` otherwise, using a stack data structure to reverse the string.
"""

def is_palindrome(string):
    """
    Determine whether a given string is a palindrome using a stack data structure.
    
    Args:
        string (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    # reverse the string
    stack = []
    for char in string:
        stack.append(char)

    rev_string = ""
    while stack:
        rev_string = rev_string + stack.pop()

    # compare reversed string with original string
    return rev_string == string