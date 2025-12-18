"""
QUESTION:
Write a function called `string_reorder` that takes a string as input and returns the string reordered alphabetically along with a dictionary containing the count of each character occurrence in the string. The function should consider spaces and other characters as part of the string.
"""

def string_reorder(string):
    sorted_string = ''.join(sorted(string))
    char_dict = {}
    for char in sorted_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return sorted_string, char_dict