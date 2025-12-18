"""
QUESTION:
Implement a function `replace_chars` that takes a string and two lists of characters as input, `char_old_list` and `char_new_list`. The function should replace each character in the string that matches a character in `char_old_list` with the corresponding character in `char_new_list`. The function should return an error message if the lengths of `char_old_list` and `char_new_list` are not equal. The function should support Unicode characters with varying byte-widths.
"""

def replace_chars(string, char_old_list, char_new_list):
    if len(char_old_list) != len(char_new_list):
        return "The length of the old characters list and new characters list must be the same."
    
    for old_char, new_char in zip(char_old_list, char_new_list):
        string = string.replace(old_char, new_char)
    return string