"""
QUESTION:
Write a function named `compare_binary_strings` that takes two binary strings `str1` and `str2` as input and returns the number of differences between them. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input strings. If the lengths of the two strings are not equal, the function should return -1. The function should not use any built-in functions for comparing characters.
"""

def compare_binary_strings(str1, str2):
    if len(str1) != len(str2):
        return -1
    differences = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            differences += 1
    return differences