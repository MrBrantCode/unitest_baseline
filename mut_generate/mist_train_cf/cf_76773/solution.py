"""
QUESTION:
Create a function called `validate_string` that checks if all alphabetic characters in a given input string are unique. The function should return `True` if all alphabetic characters are unique and `False` otherwise.
"""

def validate_string(input_string):
    alphabetic_entities = [char for char in input_string if char.isalpha()]
    unique_alphabetic_entities = set(alphabetic_entities)
    return len(alphabetic_entities) == len(unique_alphabetic_entities)