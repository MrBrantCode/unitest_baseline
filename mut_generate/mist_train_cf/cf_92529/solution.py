"""
QUESTION:
Write a Python function `filter_strings(lst, length)` that filters a given list of strings `lst` and returns the list with the strings having length greater than the given `length` and containing only alphanumeric characters.
"""

def entrance(lst, length):
    filtered_list = []
    for string in lst:
        if len(string) > length and string.isalnum():
            filtered_list.append(string)
    return filtered_list