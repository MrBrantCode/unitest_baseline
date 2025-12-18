"""
QUESTION:
Create a function `is_rotation` that checks if two given strings are rotations of each other. The function should take two strings, `string1` and `string2`, as input, where each string consists of lowercase alphabets and/or digits. The function should return `True` if `string1` and `string2` are rotations of each other, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the longer string among `string1` and `string2`, and should not use any built-in string rotation or substring functions. The length of each string is between 1 and 10^5.
"""

def is_rotation(string1: str, string2: str) -> bool:
    # Check if the lengths of the strings are equal
    if len(string1) != len(string2):
        return False
    
    # Concatenate string1 with itself
    concatenated_string = string1 + string1
    
    # Check if string2 is a substring of the concatenated string
    if string2 in concatenated_string:
        return True
    
    return False