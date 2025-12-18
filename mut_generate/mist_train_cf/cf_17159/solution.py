"""
QUESTION:
Implement a function `is_rotation(str1, str2)` that checks if `str2` is a rotation of `str1`. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input strings. The function should handle strings of length up to 10^6 efficiently, use a constant amount of additional memory, and not rely on built-in string manipulation functions or libraries. It should also handle Unicode characters correctly and be resistant to timing attacks.
"""

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    concatenated_string = str1 + str1
    return str2 in concatenated_string