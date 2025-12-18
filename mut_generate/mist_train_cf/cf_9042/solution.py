"""
QUESTION:
Write a function named `remove_odd_index_chars` that takes a string `s` as input. The function should return a modified string where all characters at odd index values are removed, excluding any punctuation marks.
"""

import string

def remove_odd_index_chars(s):
    # Create a string of all punctuation marks
    punctuations = string.punctuation
    
    # Initialize an empty string to store the modified string
    modified_string = ""
    
    # Iterate over each character in the input string
    for i, char in enumerate(s):
        # Ignore punctuation marks
        if char in punctuations:
            continue
        
        # Remove characters with odd index values
        if i % 2 == 0:
            modified_string += char
    
    return modified_string