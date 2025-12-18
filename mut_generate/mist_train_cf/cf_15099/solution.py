"""
QUESTION:
Create a function `remove_spaces_and_punctuation(s)` that takes a string `s` as input and returns a string containing only the alphanumeric characters from `s`. The function should have a time complexity of O(n), where n is the length of `s`, and should not use any built-in string manipulation functions or regular expressions.
"""

def remove_spaces_and_punctuation(s):
    # Create an empty string to store the modified string
    modified_string = ""
    
    # Iterate over each character in the input string
    for char in s:
        # Check if the character is alphanumeric (uppercase or lowercase letter, digit)
        if char.isalpha() or char.isdigit():
            # Append the alphanumeric character to the modified string
            modified_string += char
    
    # Return the modified string
    return modified_string