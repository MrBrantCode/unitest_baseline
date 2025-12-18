"""
QUESTION:
Write a function `compare_strings(str1, str2)` that takes two strings `str1` and `str2` as input and returns the number of different characters in the strings. The function should have a time complexity of O(n), where n is the length of the longer string, and a space complexity of O(1).
"""

def compare_strings(str1, str2):
    length = max(len(str1), len(str2))
    count = 0
    for i in range(length):
        if i >= len(str1) or i >= len(str2) or str1[i] != str2[i]:
            count += 1
    return count