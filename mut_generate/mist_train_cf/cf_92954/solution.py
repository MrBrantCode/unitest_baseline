"""
QUESTION:
Write a function `longest_common_prefix(strings)` that finds the longest common prefix among a given set of strings. The function should return the longest common prefix as a string. The function should have a time complexity of O(n * m), where n is the number of strings in the set and m is the length of the longest string.
"""

def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for i in range(1, len(strings)):
        while strings[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix