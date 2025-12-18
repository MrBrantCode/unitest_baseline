"""
QUESTION:
Create a function called `count_characters` that takes a string as input and returns a dictionary where each key is a unique character from the input string and the corresponding value is the count of its occurrences in the string.
"""

def count_characters(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count