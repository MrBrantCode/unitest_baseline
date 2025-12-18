"""
QUESTION:
Create a function `remove_whitespace` that takes a string as input and returns a new string with all whitespace characters removed without using any built-in string manipulation functions or regular expressions. The function should handle strings containing one or more whitespace characters.
"""

def remove_whitespace(string):
    # Create an empty string to store the characters without whitespace
    new_string = ""

    # Iterate through each character in the given string
    for char in string:
        # Check if the character is a whitespace
        if char != " ":
            # Append the character to the new string
            new_string += char
    
    return new_string