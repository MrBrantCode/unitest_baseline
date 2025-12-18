"""
QUESTION:
Write a function `longest_common_substring_length(s1, s2)` that returns the length of the longest common substring between two strings `s1` and `s2`. The function should be case-insensitive and handle special characters by considering accented and non-accented characters as equal. The function should have a time complexity of O(n), where n is the length of the shorter string, and a space complexity of O(1).
"""

def longest_common_substring_length(s1, s2):
    s1 = s1.lower()  # convert both strings to lowercase
    s2 = s2.lower()
    length = 0  # variable to store the length of the longest common substring
    start = 0  # variable to store the starting index of the current common substring
    max_length = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            length += 1
            max_length = max(max_length, length)
        else:
            length = 0
    return max_length