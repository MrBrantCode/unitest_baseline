"""
QUESTION:
Create a function named `count_characters` that takes a string as input and returns a dictionary where each key is a character from the string and its corresponding value is the number of times the character appears in the string. The function should be case-sensitive and count spaces and special characters.
"""

def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count