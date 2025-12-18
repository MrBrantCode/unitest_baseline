"""
QUESTION:
Implement a function `compare_strings(str1, str2)` that takes two strings as arguments and returns `True` if the strings are equal and `False` otherwise. The function must compare the strings character by character without using built-in string comparison functions or operators, and must have a time complexity of O(n), where n is the length of the longest string.
"""

def compare_strings(str1, str2):
    p1 = 0
    p2 = 0

    while p1 < len(str1) and p2 < len(str2):
        if str1[p1] != str2[p2]:
            return False
        p1 += 1
        p2 += 1

    return p1 == len(str1) and p2 == len(str2)