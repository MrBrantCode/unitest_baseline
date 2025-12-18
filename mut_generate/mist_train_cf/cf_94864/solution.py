"""
QUESTION:
Create a function `count_characters` that takes a string as input and returns a dictionary where each key is a character from the string and its corresponding value is the count of its occurrence. All characters, including special characters, whitespace, and punctuation marks, should be treated as separate keys.
"""

def count_characters(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count