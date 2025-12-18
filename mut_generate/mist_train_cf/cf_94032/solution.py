"""
QUESTION:
Write a function `longest_substring` that takes a string and a threshold as input. The function should return the length of the longest substring of the input string that does not contain duplicate characters within the given threshold distance. If the input string contains non-alphabetic characters or is empty, the function should return an error message.
"""

import re

def longest_substring(string, threshold):
    # Check if the input string is empty or consists only of non-alphabetic characters
    if not string or not re.search('[a-zA-Z]', string):
        return "Error: Input string is empty or consists only of non-alphabetic characters."
    
    # Check if the input string contains non-alphabetic characters
    if not string.isalpha():
        return "Error: Input string contains non-alphabetic characters."
    
    # Initialize variables
    longest_length = 0
    current_length = 0
    current_substring = ''
    previous_chars = {}
    
    # Iterate over each character in the input string
    for char in string:
        # Check if the current character is within the threshold distance of any previous character
        if char in previous_chars and previous_chars[char] >= current_length - threshold:
            # Reset the current substring and length
            current_substring = ''
            current_length = 0
        
        # Add the current character to the current substring
        current_substring += char
        
        # Update the current length
        current_length += 1
        
        # Update the previous_chars dictionary with the current character and its index
        previous_chars[char] = current_length - 1
        
        # Update the longest length if the current length is greater
        if current_length > longest_length:
            longest_length = current_length
    
    return longest_length