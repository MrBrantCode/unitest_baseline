"""
QUESTION:
Write a function named `check_substring` that takes two strings `string1` and `string2` as input and returns the number of occurrences of `string2` within `string1`, considering cases where `string2` contains multiple occurrences of characters from `string1`.
"""

def check_substring(string1, string2):
    count = 0
    i = 0
    while i < len(string1):
        j = 0
        while i < len(string1) and j < len(string2) and string1[i] == string2[j]:
            i += 1
            j += 1
        if j == len(string2):
            count += 1
        else:
            i -= j - 1
        i += 1
    return count