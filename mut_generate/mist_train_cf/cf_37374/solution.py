"""
QUESTION:
Implement a function `count_unique_characters` that takes a string as input, ignores spaces, and returns a dictionary where the keys are the unique characters (case-insensitive) and the values are the counts of each character.
"""

def count_unique_characters(input_string):
    char_count = {}
    input_string = input_string.replace(" ", "").lower()
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count