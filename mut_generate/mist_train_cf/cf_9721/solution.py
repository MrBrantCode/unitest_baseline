"""
QUESTION:
Develop a function `longest_common_prefix(strings)` that takes a list of strings as input and returns the longest common prefix string. The function should have a time complexity of O(N*M), where N is the length of the list of strings and M is the average length of the strings. The function should use O(M) extra space, where M is the maximum length of the strings. The function should handle any character encoding, including Unicode, and should be efficient and optimized to handle large inputs (up to 10^6 strings, with a maximum length of 10^4 characters each).
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