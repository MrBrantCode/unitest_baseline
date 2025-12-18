"""
QUESTION:
Implement a function `has_unique_chars(string)` that determines whether a given string has all unique characters. The function should have a time complexity of O(n) and a space complexity of O(1). Assume the input string only contains ASCII characters.
"""

def has_unique_chars(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    
    for char in string:
        ascii_value = ord(char)
        
        if char_set[ascii_value]:
            return False
        
        char_set[ascii_value] = True
    
    return True