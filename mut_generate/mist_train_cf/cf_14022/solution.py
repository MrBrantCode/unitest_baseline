"""
QUESTION:
Write a function `remove_occurrences(string, letter)` that takes a string and a letter as input and returns a new string where all occurrences of the given letter that are immediately followed by a digit have been removed.
"""

def remove_occurrences(string, letter):
    modified_string = ''
    i = 0
    while i < len(string):
        if string[i] == letter and i+1 < len(string) and string[i+1].isdigit():
            i += 2
            continue
        modified_string += string[i]
        i += 1
    return modified_string