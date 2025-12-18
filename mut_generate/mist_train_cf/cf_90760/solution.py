"""
QUESTION:
Create a function `get_character_indices` that takes a string as input and returns a dictionary where the keys are the unique characters in the string and the values are lists containing the indices of each occurrence of the character in the string. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def get_character_indices(s):
    character_indices = {}
    
    for index, character in enumerate(s):
        if character not in character_indices:
            character_indices[character] = [index]
        else:
            character_indices[character].append(index)
    
    return character_indices