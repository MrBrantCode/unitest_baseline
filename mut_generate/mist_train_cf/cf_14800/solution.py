"""
QUESTION:
Create a function named `split_string` that takes two parameters: a string and a separator. The function should split the input string into substrings based on the given separator and return the resulting substrings in a list. The function should handle cases where the separator occurs at the beginning or end of the string, and consecutive separators should not result in empty substrings in the output.
"""

def split_string(s, sep):
    result = []
    current_substring = ""
    for char in s:
        if char == sep:
            if current_substring:
                result.append(current_substring)
            current_substring = ""
        else:
            current_substring += char
    if current_substring:
        result.append(current_substring)
    return result