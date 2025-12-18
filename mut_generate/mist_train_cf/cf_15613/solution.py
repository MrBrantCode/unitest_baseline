"""
QUESTION:
Implement a method `isUnique` that checks if a given string of printable ASCII characters has all unique characters. The method should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), without using additional data structures, built-in functions, or libraries that directly solve the problem. The input string cannot be modified and sorting algorithms cannot be used.
"""

def isUnique(string):
    # If the length of the string is greater than 128, it means that it contains repeated characters.
    if len(string) > 128:
        return False
    
    # Create a boolean array of size 128 to keep track of characters encountered.
    char_set = [False] * 128
    
    # Iterate through each character in the string.
    for char in string:
        # Get the ASCII value of the character.
        ascii_val = ord(char)
        # If the character has already been encountered, return False.
        if char_set[ascii_val]:
            return False
        # Mark the character as encountered.
        char_set[ascii_val] = True
    
    # If no repeated characters were encountered, return True.
    return True