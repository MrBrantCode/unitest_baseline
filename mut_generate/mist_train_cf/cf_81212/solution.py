"""
QUESTION:
Write a function `remove_alpha_at_index` that takes a list of strings and an integer index as input. The function should return a new list where all alphabetic characters at the specified index are removed from the original strings. The function should handle strings of varying lengths and strings containing special characters. If a string is shorter than the specified index, it should be included in the output list unchanged.
"""

def remove_alpha_at_index(string_list, index):
    new_list = []
    for string in string_list:
        if len(string) > index and string[index].isalpha():
            string = string[:index] + string[index+1:]
        new_list.append(string)
    return new_list