"""
QUESTION:
Write a function `filter_strings_by_character` that takes a list of strings and a character as input, and returns a list of strings that start and end with the specified character. The returned list should be in reverse order.
"""

def filter_strings_by_character(my_list, character):
    filtered_list = [string for string in my_list if string.startswith(character) and string.endswith(character)]
    return filtered_list[::-1]