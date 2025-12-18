"""
QUESTION:
Implement a function named `alternate_strings` that takes two strings `s1` and `s2` as input. If the lengths of `s1` and `s2` are different, the function should return a new string consisting of alternating characters from `s1` and `s2`, with the remaining characters of the longer string appended at the end. If `s1` and `s2` are of the same length, the function should return a string consisting of characters only from `s1`.
"""

def alternate_strings(s1, s2):
    result = ""
    if len(s1) > len(s2):
        for i in range(len(s2)):
            result += s1[i] + s2[i]
        result += s1[len(s2):]
    elif len(s1) < len(s2):
        for i in range(len(s1)):
            result += s1[i] + s2[i]
        result += s2[len(s1):]
    else:
        for i in range(len(s1)):
            result += s1[i]
    return result