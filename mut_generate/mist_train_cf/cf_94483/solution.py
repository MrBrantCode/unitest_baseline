"""
QUESTION:
Write a function named `filter_strings_by_character` that takes a list of strings (`my_list`) and a character as input. The function should return a list of strings that start and end with the specified character, in reverse order.
"""

def filter_strings_by_character(my_list, character):
    filtered_list = [string for string in my_list if string.startswith(character) and string.endswith(character)]
    return filtered_list[::-1]