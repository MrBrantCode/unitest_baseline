"""
QUESTION:
Implement a function called "longest_common_substring" that takes two strings as input and returns the longest common substring found between them. The function should be case-insensitive, meaning that uppercase and lowercase characters should be considered equal. If there are multiple substrings with the same length, return the one that appears first in the first string. The input strings will only contain alphanumeric characters and spaces with no leading or trailing spaces and may have different lengths.
"""

def longest_common_substring(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    max_length = 0
    result = ""

    for i in range(len(s1)):
        for j in range(i, len(s1)):
            substring = s1[i:j+1]
            if substring in s2 and len(substring) > max_length:
                max_length = len(substring)
                result = substring

    return result