"""
QUESTION:
Write a Python function `reverse_string` that takes a string as input and prints its reverse. The function should validate if the input is a valid string and raise an exception if it's not. Implement a recursive approach for reversing the string.
"""

class InvalidStringException(Exception):
    pass

def reverse_string(s):
    if not isinstance(s, str):
        raise InvalidStringException("Input is not a valid string.")
    
    def reverse_helper(string):
        if len(string) <= 1:
            return string
        else:
            return reverse_helper(string[1:]) + string[0]
    
    return reverse_helper(s)