"""
QUESTION:
Create a function `find_strings_with_target` that takes a list of strings `list_of_strings` and a `target_string` as input. The function should return a list of strings from `list_of_strings` where the `target_string` is a substring and the `target_string` is at least 3 characters long.
"""

def find_strings_with_target(list_of_strings, target_string):
    result = []
    for string in list_of_strings:
        if target_string in string and len(target_string) >= 3:
            result.append(string)
    return result