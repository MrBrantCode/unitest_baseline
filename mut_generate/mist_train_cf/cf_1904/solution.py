"""
QUESTION:
Create a function `is_pair(str1, str2)` that checks whether two input strings `str1` and `str2` contain the same characters with the same frequency, regardless of order, and are case-insensitive. The function should handle strings of any length, including those with special characters, whitespace, and Unicode characters, and should be efficient for large strings.
"""

from collections import Counter

def is_pair(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = str1.lower()
    str2 = str2.lower()

    count1 = Counter(str1)
    count2 = Counter(str2)

    return count1 == count2