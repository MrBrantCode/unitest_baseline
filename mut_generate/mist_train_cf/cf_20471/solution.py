"""
QUESTION:
Create a function `find_strings_with_target` that takes a list of strings `list_of_strings` and a target string `target_string` as input. The function should return a list of strings from `list_of_strings` that contain `target_string` as a substring, with the following restrictions:

- `target_string` must be at least 3 characters long. If not, return an empty list.
- The search is case-sensitive.
- The order of strings in the output list should match their order in the input list.
- Duplicate strings in the input list are allowed.
- Each occurrence of `target_string` in a single string should be counted separately in the output list.
"""

def find_strings_with_target(list_of_strings, target_string):
    result = []
    if len(target_string) < 3:
        return result
    for string in list_of_strings:
        if target_string in string:
            result.append(string)
    return result