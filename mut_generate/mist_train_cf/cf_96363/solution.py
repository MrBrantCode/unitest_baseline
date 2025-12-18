"""
QUESTION:
Given two strings s1 and s2, implement a function count_substring_occurrences(s1, s2) that finds the number of times a substring of s2 with length greater than or equal to 2 appears in s1. The matching should be case-sensitive and can include any printable ASCII characters.
"""

def count_substring_occurrences(s1, s2):
    count = 0
    for i in range(2, len(s2)+1):
        for j in range(len(s2)-i+1):
            sub = s2[j:j+i]
            if sub in s1:
                count += 1
    return count