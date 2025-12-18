"""
QUESTION:
Create a function named `reverse_string` that takes a string as an input, validates if it's a valid string, and raises a custom exception if it's not. The function should reverse the input string using a recursive approach and then print the reversed string. The custom exception should be raised with a message "Input is not a valid string." if the input is not a string.
"""

class InvalidStringException(Exception):
    pass

def reverse_string(s):
    if not isinstance(s, str):
        raise InvalidStringException("Input is not a valid string.")
    
    def reverse_helper(s):
        if len(s) <= 1:
            return s
        else:
            return reverse_helper(s[1:]) + s[0]
    
    return reverse_helper(s)