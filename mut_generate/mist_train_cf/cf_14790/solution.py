"""
QUESTION:
Create a function `count_characters(strings)` that takes a list of strings as input and returns the total number of alphabetic characters across all strings, excluding special characters and white spaces.
"""

def count_characters(strings):
    total_characters = 0
    special_characters = "!@#$%^&*()_+=-{}[]|:;<>,.?/~`"
    
    for string in strings:
        for char in string:
            if char.isalpha() and char not in special_characters:
                total_characters += 1
    
    return total_characters