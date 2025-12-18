"""
QUESTION:
Create a function `is_unique_string(s)` that checks if a string `s` has unique characters, where `s` only contains lowercase alphabets and has a maximum length of 10^6 characters. The function should return `True` if `s` has all unique characters, and `False` otherwise, with a time complexity of O(n) and a space complexity of O(1).
"""

def is_unique_string(s):
    if len(s) > 26:
        return False
    
    char_set = [False] * 26
    
    for char in s:
        index = ord(char) - ord('a')
        if char_set[index]:
            return False
        char_set[index] = True
    
    return True