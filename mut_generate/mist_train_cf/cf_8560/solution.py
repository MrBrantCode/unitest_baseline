"""
QUESTION:
Write a function named `char_matches` that takes two same-length strings `s1` and `s2` as input, and returns a list of characters that are the same at the same position in both strings, ignoring case. The function must be recursive and have a time complexity of O(n), where n is the length of the strings.
"""

def char_matches(s1, s2):
    if s1 == "" or s2 == "":
        return []

    if s1[0].lower() == s2[0].lower():
        return [s1[0]] + char_matches(s1[1:], s2[1:])
    else:
        return char_matches(s1[1:], s2[1:])