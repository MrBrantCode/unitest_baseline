"""
QUESTION:
Write a function `find_strings_with_target` that takes a list of strings `list_of_strings` and a target string `target_string` as input and returns a list of strings that contain the target string as a substring. The target string must be at least 3 characters long. If the target string is less than 3 characters long, return an empty list. The function should be case-sensitive and preserve the order of strings in the input list.
"""

def find_strings_with_target(list_of_strings, target_string):
    result = []
    if len(target_string) < 3:
        return result
    for string in list_of_strings:
        if target_string in string:
            result.append(string)
    return result