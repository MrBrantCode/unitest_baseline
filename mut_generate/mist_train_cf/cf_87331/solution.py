"""
QUESTION:
Write a function named `longest_common_substring` that takes two strings as input and returns the longest common substring between them. The substring should contain only alphabetic characters and should be case-sensitive. The solution should have a time complexity of O(n^3), where n is the length of the longest string.
"""

def longest_common_substring(s1, s2):
    longest_substring = ""

    for i in range(len(s1)):
        for j in range(i, len(s1)):
            substring = s1[i:j+1]
            if substring.isalpha() and substring in s2 and len(substring) > len(longest_substring):
                longest_substring = substring

    return longest_substring