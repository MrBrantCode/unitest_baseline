"""
QUESTION:
Create a function named `char_indices` that takes a string as input and returns a dictionary. The dictionary should have each unique character in the string as keys, with their corresponding values being lists of indices where each character appears in the string. The dictionary must be sorted in descending order by the characters.
"""

def char_indices(s):
    char_dict = {}
    for i, char in enumerate(s):
        if char not in char_dict:
            char_dict[char] = [i]
        else:
            char_dict[char].append(i)
    return dict(sorted(char_dict.items(), key=lambda x: x[0], reverse=True))