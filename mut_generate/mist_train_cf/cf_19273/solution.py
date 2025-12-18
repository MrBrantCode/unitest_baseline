"""
QUESTION:
Create a function named `count_characters` that takes a string as input and returns a dictionary with the count of each unique alphabetical character in the string, excluding any whitespace characters and non-alphabetical characters, and handling cases in a case-insensitive manner.
"""

def count_characters(input_string):
    input_string = input_string.replace(" ", "").lower()
    character_count = {}
    
    for char in input_string:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    
    return character_count