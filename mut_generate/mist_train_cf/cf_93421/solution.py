"""
QUESTION:
Write a function `find_matches(str1, str2, index)` that identifies character matches in the same position between two same-length strings `str1` and `str2`, without using any loops or built-in functions. The function should return a list of characters that match at the same position in both strings. The index parameter is used to keep track of the current position in the strings.
"""

def find_matches(str1, str2, index):
    if index >= len(str1) or index >= len(str2):
        return []

    matches = []
    if str1[index] == str2[index]:
        matches.append(str1[index])

    return matches + find_matches(str1, str2, index + 1)