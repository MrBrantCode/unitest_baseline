"""
QUESTION:
Implement a function called "longest_common_substring" that takes two strings as input and returns the longest common substring found between them, case-insensitive. The function should consider all possible substrings of both strings and return the longest one that appears in both strings. If there are multiple substrings with the same length, it should return the one that appears first in the first string. The input strings will only contain alphanumeric characters and spaces, with no leading or trailing spaces, and may have different lengths.
"""

def longest_common_substring(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    max_length = 0
    result = ""

    for length in range(len(s1), 0, -1):
        for i in range(len(s1) - length + 1):
            substring = s1[i:i+length]
            if substring in s2 and len(substring) > max_length:
                max_length = len(substring)
                result = substring

    return result