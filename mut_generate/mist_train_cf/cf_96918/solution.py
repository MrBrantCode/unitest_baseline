"""
QUESTION:
Create a function named `count_similar_characters` that takes two strings as input and returns the number of similar characters at the same index in both strings. The function should be case-sensitive, consider spaces as characters, and handle strings of any length, including empty strings, special characters, and numbers. The time complexity should be O(n), where n is the length of the longer string. The function should not use built-in string comparison or similarity calculation methods, additional data structures, or recursion.
"""

def count_similar_characters(string1, string2):
    count = 0
    length = max(len(string1), len(string2))
    for i in range(length):
        if i < len(string1) and i < len(string2) and string1[i] == string2[i]:
            count += 1
    return count