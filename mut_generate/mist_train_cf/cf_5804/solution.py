"""
QUESTION:
Filter a list of strings and return the list with the strings having length greater than a given number, excluding strings that contain special characters and duplicates. Implement this without using built-in Python functions or libraries for filtering and checking duplicates.

The function name is `filter_strings` and it should take two parameters: `string_list` (the list of strings to be filtered) and `length` (the minimum length for the strings to be included in the result).
"""

def filter_strings(string_list, length):
    filtered_list = []
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', ';', ':', '<', '>', '.', ',', '/', '?', '|', '\\', '`', '~']
    for string in string_list:
        if len(string) > length and not any(char in special_chars for char in string) and string not in filtered_list:
            filtered_list.append(string)
    return filtered_list