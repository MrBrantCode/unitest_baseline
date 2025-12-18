"""
QUESTION:
Write a function called `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix among all the strings in the list. The function should have a time complexity of O(n * m), where n is the number of strings in the list and m is the average length of the strings. If the input list is empty, the function should return an empty string.
"""

def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for string in strings[1:]:
        while string.startswith(prefix) is False:
            prefix = prefix[:-1]

        if prefix == "":
            return ""

    return prefix