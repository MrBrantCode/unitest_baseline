"""
QUESTION:
Implement a function `has_unique_chars(s: str) -> bool` that checks if all characters in the input string `s` are unique without using any additional data structures other than a fixed-size boolean array. Assume that the input string only contains ASCII characters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def has_unique_chars(s: str) -> bool:
    # A string with more than 128 characters must have duplicate characters (assuming ASCII chars)
    if len(s) > 128:
        return False
    
    char_set = [False] * 128
    
    for char in s:
        # Get the ASCII value of the character
        val = ord(char)
        # If the character is already in the array, it is a duplicate
        if char_set[val]:
            return False
        char_set[val] = True
    
    return True