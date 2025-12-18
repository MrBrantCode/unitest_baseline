"""
QUESTION:
Write a function `first_nonrepeating_char` that takes a string as input and returns a tuple containing the index and value of the first non-repeating alphabetic character. If the string is empty, contains only repeating characters, or contains no alphabetic characters, return -1. The function should ignore non-alphabetic characters and be case-sensitive.
"""

def first_nonrepeating_char(string):
    # Initialize a dictionary to hold character frequency
    char_count = {}
    
    # Iterate over the string and count character frequency
    for char in string:
        if char.isalpha(): # Only consider alphabetic entities
            char_count[char] = char_count.get(char, 0) + 1
    
    # Iterate over the string to find the first nonrepeating character
    for idx, char in enumerate(string):
        if char.isalpha() and char_count[char] == 1:
            return idx, char

    # If there is no nonrepeating character or if string is empty, return -1
    return -1