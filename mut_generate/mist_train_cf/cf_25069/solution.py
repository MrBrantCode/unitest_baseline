"""
QUESTION:
Create a function named `is_substring_present` that takes two parameters: `string` and `sub_string`. The function should determine if `sub_string` is present in `string` and return a boolean value.
"""

def is_substring_present(string, sub_string):
    for i in range(len(string)):
        if string[i : (i + len(sub_string))] == sub_string:
            return True
    return False