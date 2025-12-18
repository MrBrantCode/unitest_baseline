"""
QUESTION:
Create a function `duplicate_characters(string)` that takes a string as input and returns a dictionary where the keys are duplicate characters in the string and the values are lists of indices where each character appears. The function should exclude characters that do not have any duplicates. The function should also have a time complexity of O(n), where n is the length of the string.
"""

def duplicate_characters(string):
    char_to_indices = {}
    for i, char in enumerate(string):
        if char not in char_to_indices:
            char_to_indices[char] = [i]
        else:
            char_to_indices[char].append(i)
            
    return {char: indices for char, indices in char_to_indices.items() if len(indices) > 1}