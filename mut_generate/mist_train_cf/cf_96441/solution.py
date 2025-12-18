"""
QUESTION:
Write a function `longest_common_substring_length(s1, s2)` that takes two strings `s1` and `s2` as input and returns the length of the longest common substring between them. The function should have a time complexity of O(n), where n is the length of the shorter string, and a space complexity of O(1). It should handle case-insensitive strings, special characters, and multiple occurrences of the same substring within a string.
"""

def longest_common_substring_length(s1, s2):
    s1 = s1.lower()  # convert both strings to lowercase
    s2 = s2.lower()
    len_s1 = len(s1)
    len_s2 = len(s2)
    max_len = 0  # variable to store the length of the longest common substring
    
    for i in range(len_s1):
        match_len = 0  # variable to store the length of the current match
        for j in range(len_s2):
            k = 0
            while i + k < len_s1 and j + k < len_s2 and s1[i + k] == s2[j + k]:
                match_len = k + 1
                k += 1
            if match_len > max_len:
                max_len = match_len
    return max_len