"""
QUESTION:
Find the longest common substring between two strings `s1` and `s2` that contains only alphabetic characters and is case-sensitive. The function should have a time complexity of O(n^3), where n is the length of the longest string.
"""

def find_longest_common_substring(s1, s2):
    longest_substring = ""

    for i in range(len(s1)):
        for j in range(i, len(s1)):
            substring = s1[i:j+1]
            if substring in s2 and len(substring) > len(longest_substring) and substring.isalpha():
                longest_substring = substring

    return longest_substring