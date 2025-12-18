"""
QUESTION:
Create a function named `count_characters` that takes a string as input and returns a dictionary with the count of all non-whitespace characters in the string in a case-insensitive manner. The function should ignore any whitespace characters in the string and treat uppercase and lowercase characters as the same.
"""

def count_characters(string):
    string = string.lower()
    char_count = {}
    for char in string:
        if char.isspace():
            continue
        char_count[char] = char_count.get(char, 0) + 1
    return char_count