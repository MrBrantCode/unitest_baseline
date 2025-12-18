"""
QUESTION:
Create a function named `has_unique_chars` that checks whether a string consists of all unique ASCII characters. The function should have a time complexity of O(n), where n is the number of characters in the string, and a space complexity of O(1). Assume the input string contains only ASCII characters.
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