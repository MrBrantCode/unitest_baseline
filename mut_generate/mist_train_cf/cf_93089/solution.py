"""
QUESTION:
Create a function `char_indices(string)` that takes a string as input and returns a dictionary where each character in the string is a key and the corresponding value is a list of indices where the character appears in the string. The dictionary should be sorted in alphabetical order by the characters.
"""

def char_indices(string):
    char_dict = {}
    for index, char in enumerate(string):
        if char in char_dict:
            char_dict[char].append(index)
        else:
            char_dict[char] = [index]
    return dict(sorted(char_dict.items()))