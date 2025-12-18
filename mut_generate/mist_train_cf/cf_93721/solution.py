"""
QUESTION:
Create a function `get_char_indices` that takes a string as input and returns a dictionary where the keys are the unique letter characters in the string (both uppercase and lowercase) and the values are lists containing the indices of each occurrence of the character in the string. The function should ignore any non-letter characters and have a time complexity of O(n), where n is the length of the input string.
"""

def get_char_indices(s):
    char_indices = {}
    for i, char in enumerate(s):
        if char.isalpha():
            char = char.lower()
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)
    return char_indices