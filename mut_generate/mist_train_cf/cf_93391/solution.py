"""
QUESTION:
Create a function `split_string(string, separator)` that splits a given string into substrings based on a specified separator, which can be any combination of characters and can occur multiple times within the string. The function should handle cases where the separator occurs at the beginning or end of the string, and consecutive separators should not result in empty substrings in the output.
"""

def split_string(string, separator):
    result = []
    current_substring = ""
    for char in string:
        if char in separator:
            if current_substring != "":
                result.append(current_substring)
            current_substring = ""
        else:
            current_substring += char
    if current_substring != "":
        result.append(current_substring)
    return result