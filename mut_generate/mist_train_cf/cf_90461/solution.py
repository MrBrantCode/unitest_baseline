"""
QUESTION:
Implement a function `char_matches(s1, s2)` that takes two strings of the same length as input and returns a list of characters that match in the same position, case-insensitively. The function must be implemented recursively, have a time complexity of O(n), where n is the length of the strings, and cannot use any loops or built-in functions except for slicing and the `lower()` method.
"""

def char_matches(s1, s2):
    # Base case: If either string is empty, there are no matches
    if s1 == "" or s2 == "":
        return []

    # Compare the first characters of the strings case-insensitively
    if s1[0].lower() == s2[0].lower():
        # If there is a match, add the character to the result and recurse on the rest of the strings
        return [s1[0]] + char_matches(s1[1:], s2[1:])
    else:
        # If there is no match, simply recurse on the rest of the strings
        return char_matches(s1[1:], s2[1:])