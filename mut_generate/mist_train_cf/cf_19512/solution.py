"""
QUESTION:
Write a function `check_if_string(obj)` that takes an object as input and returns `True` if the object is a string and `False` otherwise. The function must use bitwise operations and cannot use any built-in type checking functions or operators. Assume the input object is a string if its first character has a valid ASCII or Unicode value.
"""

def check_if_string(obj):
    try:
        # Convert the first character to its ASCII/Unicode value
        first_char = ord(obj[0])
        
        # Check if the ASCII/Unicode value is within the valid range for characters
        if first_char >= 0 and first_char <= 127:
            return True
        else:
            return False
    except:
        return False