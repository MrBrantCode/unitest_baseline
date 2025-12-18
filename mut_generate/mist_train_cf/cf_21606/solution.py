"""
QUESTION:
Write a function `longest_common_prefix(strings)` that finds the longest common prefix among a given set of strings. The function should have a time complexity of O(n * m), where n is the number of strings in the set and m is the average length of the strings. If the given set of strings is empty, the function should return an empty string.
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