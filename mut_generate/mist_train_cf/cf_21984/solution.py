"""
QUESTION:
Create a function called `char_indices` that takes a string as input and returns a dictionary. Each character in the string should be a key in the dictionary, with its corresponding value being a list of indices where the character appears in the string. The dictionary should be sorted in descending order by the characters.
"""

def char_indices(string):
    char_dict = {}
    for i, char in enumerate(string):
        if char not in char_dict:
            char_dict[char] = [i]
        else:
            char_dict[char].append(i)
    return dict(sorted(char_dict.items(), key=lambda x: x[0], reverse=True))