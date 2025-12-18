"""
QUESTION:
Create a function named `count_characters` that takes a string as input and returns a dictionary where the keys are the unique characters in the string and the values are their corresponding counts.
"""

def count_characters(input_string):
    character_count = {}
    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count