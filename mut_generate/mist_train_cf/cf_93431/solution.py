"""
QUESTION:
Create a function `is_unique_string(s)` that checks if a given string `s` has all unique characters. The function should return `True` if the string has unique characters and `False` otherwise. The input string `s` will only contain lowercase alphabets and can have a maximum length of 10^6 characters. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
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