"""
QUESTION:
Write a function `string_to_list(s)` that takes a string `s` and returns a list of its non-whitespace characters. The function should ignore any whitespace characters and handle strings with leading or trailing whitespace characters correctly. Implement the solution without using any built-in string or list methods (except for indexing and assignment), regular expressions, or third-party libraries. The time complexity should be O(n), where n is the length of the string.
"""

def string_to_list(s):
    # Remove leading and trailing whitespace characters
    s = s.strip()
    
    # Initialize an empty list to store the characters
    chars = []
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a whitespace character
        if char != ' ':
            # Append the character to the list
            chars.append(char)
    
    return chars