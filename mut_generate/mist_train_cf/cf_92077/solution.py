"""
QUESTION:
Write a function named `count_alphabets` that takes an input string and returns the count of alphabets in the string, considering uppercase and lowercase letters as separate entities, and ignoring any punctuation marks, special characters, and non-English alphabets.
"""

import string

def count_alphabets(input_string):
    # Initialize a counter variable
    count = 0
    
    # Remove any whitespace characters
    input_string = input_string.replace(" ", "")
    
    # Remove punctuation marks and special characters
    input_string = ''.join(char for char in input_string if char.isalpha())
    
    # Check each character in the string
    for char in input_string:
        # Increment the counter if the character is an alphabet
        if char.isalpha():
            count += 1
    
    return count