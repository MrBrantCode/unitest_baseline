"""
QUESTION:
Write a function `sort_and_convert_list(strings)` that takes a list of strings as input. The function should remove duplicates, sort the strings in descending order of length, and convert the result to uppercase. The function should return the resulting list of strings.
"""

def sort_and_convert_list(strings):
    unique_strings = list(set(strings))
    sorted_strings = sorted(unique_strings, key=lambda x: len(x), reverse=True)
    uppercase_strings = [string.upper() for string in sorted_strings]
    return uppercase_strings