"""
QUESTION:
Write a function named `find_strings_with_substring` that takes a list of strings and a string as input and returns a list of strings from the input list that contain the given string as a substring. The search for substrings should be case-sensitive. The function should not include duplicate strings in the output list, even if the substring appears multiple times in a string.
"""

def find_strings_with_substring(strings, substring):
    result = []
    for string in strings:
        if substring in string and string not in result:
            result.append(string)
    return result