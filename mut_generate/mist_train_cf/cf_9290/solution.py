"""
QUESTION:
Implement a function `has_unique_chars` to check if a given string has all unique characters with a time complexity of O(n) and a space complexity of O(1). Assume the input string only contains ASCII characters.
"""

def has_unique_chars(string):
    # If the string has more than 128 characters,
    # it must have repeated characters.
    if len(string) > 128:
        return False
    
    # Create an array of 128 booleans, initialized to False.
    # The index represents the ASCII value of a character,
    # and the value at that index represents whether that
    # character has been encountered before or not.
    char_set = [False] * 128
    
    # Iterate through each character in the string.
    for char in string:
        # Get the ASCII value of the character.
        ascii_value = ord(char)
        
        # If the character has already been encountered before,
        # return False.
        if char_set[ascii_value]:
            return False
        
        # Mark the character as encountered.
        char_set[ascii_value] = True
    
    # If no characters were encountered twice,
    # return True.
    return True