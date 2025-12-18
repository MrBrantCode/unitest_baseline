"""
QUESTION:
Write a function called `longest_common_substring_length` that takes two strings `s1` and `s2` as input and returns the length of the longest common substring between the two strings. The function should have a time complexity of O(n^2), where n is the length of the longer string, and a space complexity of O(1), using only a few variables and no additional data structures.
"""

def longest_common_substring_length(s1, s2):
    m = len(s1)
    n = len(s2)
    
    max_length = 0
    
    for i in range(m):
        for j in range(n):
            length = 0
            while i + length < m and j + length < n and s1[i + length] == s2[j + length]:
                length += 1
            max_length = max(max_length, length)
    
    return max_length