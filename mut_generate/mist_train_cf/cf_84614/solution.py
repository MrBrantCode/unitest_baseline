"""
QUESTION:
Write a function `sort_strings_in_list` that sorts the string elements in a given list alphabetically while leaving the non-string elements in their original positions. The function should take a list containing a mix of integers and strings as input and return the modified list with sorted string elements.
"""

def sort_strings_in_list(mixed_list):
    str_indices = [i for i, x in enumerate(mixed_list) if type(x) == str]
    str_list = sorted([x for x in mixed_list if type(x) == str])
    
    for i, index in enumerate(str_indices):
        mixed_list[index] = str_list[i]
    
    return mixed_list