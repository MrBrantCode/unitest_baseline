"""
QUESTION:
Create a function called `get_char_indices` that takes a string as input and returns a dictionary where the keys are the unique alphabetic characters in the string and the values are lists containing the indices of each occurrence of the character in the string. Uppercase and lowercase letters should be handled as separate characters. The function should ignore non-alphabetic characters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def get_char_indices(string):
    char_indices = {}
    for i, char in enumerate(string):
        if char.isalpha():
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)
    return char_indices