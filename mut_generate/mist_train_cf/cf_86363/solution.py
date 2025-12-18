"""
QUESTION:
Write a function `has_unique_chars` that checks if a string contains all unique ASCII characters. The function should not use any additional data structures or libraries and should have a time complexity of O(n) and a space complexity of O(1). The input string is assumed to only contain ASCII characters.
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