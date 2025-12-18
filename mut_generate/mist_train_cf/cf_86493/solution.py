"""
QUESTION:
Implement a method named `is_unique` that checks if a given string of printable ASCII characters has all unique characters. The method should have a time complexity of O(n) and a space complexity of O(1). It should work for uppercase and lowercase letters as different characters, without converting the input string to lowercase or uppercase, and without using additional data structures, built-in functions, libraries, sorting algorithms, recursion, bitwise operators, or bit manipulation.
"""

def is_unique(string):
    # If the string has more than 128 characters, it must have repeated characters
    if len(string) > 128:
        return False
    
    # Create a boolean array to store the presence of each character
    # Initialize all values as False
    char_set = [False] * 128
    
    # Iterate through each character in the string
    for char in string:
        # Get the ASCII value of the character
        ascii_value = ord(char)
        
        # If the character has already been seen, return False
        if char_set[ascii_value]:
            return False
        
        # Mark the character as seen
        char_set[ascii_value] = True
    
    # If no repeated characters were found, return True
    return True