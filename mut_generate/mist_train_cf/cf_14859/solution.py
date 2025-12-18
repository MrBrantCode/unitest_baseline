"""
QUESTION:
Write a recursive function `find_matches` that takes two strings of the same length and returns a list of characters that are in the same position in both strings, without using loops or built-in functions. The function should also take an index to keep track of the current position in the strings.
"""

def find_matches(str1, str2, index):
    if index >= len(str1) or index >= len(str2):
        return []

    matches = []
    if str1[index] == str2[index]:
        matches.append(str1[index])

    return matches + find_matches(str1, str2, index + 1)