"""
QUESTION:
Create a function `string_compare(str1, str2)` that takes two strings as arguments and returns `True` if the strings are equal and `False` otherwise. The function must compare the strings character by character without using any built-in string comparison functions or operators (such as `==`, `!=`, or `strcmp`). The function should also handle strings of different lengths and return `False` in such cases.
"""

def string_compare(str1, str2):
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Iterate over each character in the strings and compare them
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    
    # All characters are equal, so the strings are equal
    return True