"""
QUESTION:
Create a function named `count_characters` that takes a string as input and returns a dictionary containing the frequency of each character in the string, considering both uppercase and lowercase letters, special characters, and whitespace.
"""

def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count