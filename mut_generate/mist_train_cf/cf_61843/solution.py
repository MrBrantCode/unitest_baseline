"""
QUESTION:
Create a function named `filter_elements` that takes two parameters: a list of strings and a character. The function should return a list of strings that contain the given character.
"""

def filter_elements(elements, character):
    filtrated_sequence = [element for element in elements if character in element] 
    return filtrated_sequence