"""
QUESTION:
Write a function `has_unique_chars` that checks whether a given string has all unique ASCII characters. The function should not use any additional data structures or libraries, have a time complexity of O(n), and a space complexity of O(1), where n is the length of the input string.
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