"""
QUESTION:
Implement a function `compare_strings(str1, str2)` that compares two input strings `str1` and `str2` and returns "yes" if they are equal, otherwise returns "no". The comparison should be case-sensitive. The function should have a time complexity of O(n), where n is the length of the longer string, and should not use any built-in string comparison functions or methods.
"""

def entrance(str1, str2):
    if len(str1) != len(str2):
        return "no"

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return "no"

    return "yes"