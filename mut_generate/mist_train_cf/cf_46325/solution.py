"""
QUESTION:
Write a function called `custom_string_replace` that takes three parameters: `target_string`, `substitute_string`, and `base_string`. The function should iterate through `base_string` and replace the first occurrence of `target_string` with `substitute_string`. If `target_string` is not found in `base_string`, return `base_string` as it is. The function should not use any built-in string replacing functions.
"""

def custom_string_replace(target_string, substitute_string, base_string):
    new_string = ''
    i = 0
    while i < len(base_string):
        if base_string[i : i + len(target_string)] == target_string:
            new_string += substitute_string
            i += len(target_string)
            break
        else:
            new_string += base_string[i]
            i += 1
    if i < len(base_string):
        new_string += base_string[i:]
    return new_string