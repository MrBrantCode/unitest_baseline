"""
QUESTION:
Write a function named `first_non_repeating_char` that takes a string `input_str` as input and returns the first non-repeating character in the string without using any built-in Python functions or libraries. If no non-repeating character is found, return `None`.
"""

def firstNonRepeatingChar(input_str):
    char_count = {}  # dictionary to store character count
    
    # iterate over the string and count the occurrences of each character
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # iterate over the string again and return the first character with count 1
    for char in input_str:
        if char_count[char] == 1:
            return char
    
    # if no non-repeating character found, return None
    return None