"""
QUESTION:
Write a function named "remove_special_chars" that takes a string as input and returns the modified string without any spaces, punctuation, or special characters, only containing alphanumeric characters. The function should be able to handle strings of any length and any combination of characters, maintaining the original order, and have a time complexity of O(n), where n is the length of the input string. The input string will not be empty.
"""

def remove_special_chars(s):
    # Initialize an empty string to store the modified string
    modified_string = ""
    
    # Iterate over each character in the input string
    for char in s:
        # Check if the character is alphanumeric
        if char.isalnum():
            # Append the alphanumeric character to the modified string
            modified_string += char
    
    # Return the modified string
    return modified_string