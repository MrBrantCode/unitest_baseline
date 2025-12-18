"""
QUESTION:
Write a function `sort_strings` that takes a list of mixed variable types as input, sorts the strings alphabetically, and keeps the non-strings (including integers) in their original order at the beginning of the list. The function should ignore the non-strings when sorting and maintain their original positions relative to each other.
"""

def sort_strings(mix_list):
    string_list = sorted([x for x in mix_list if isinstance(x, str)])
    non_string_list = [x for x in mix_list if not isinstance(x, str)]
    return non_string_list + string_list