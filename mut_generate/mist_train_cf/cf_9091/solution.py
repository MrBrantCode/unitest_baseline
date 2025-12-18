"""
QUESTION:
Write a function named `has_unique_chars` that checks whether a given string has all unique ASCII characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string. The function should return `True` if all characters are unique and `False` otherwise.
"""

def has_unique_chars(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    
    for char in string:
        ascii_val = ord(char)
        
        if char_set[ascii_val]:
            return False
        
        char_set[ascii_val] = True
    
    return True