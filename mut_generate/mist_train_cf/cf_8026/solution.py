"""
QUESTION:
Write a function named `longest_common_substring` that takes two strings `s1` and `s2` as input and returns the longest common substring that consists of only uppercase letters. The function should have a time complexity of O(n^2), where n is the length of the longest input string.
"""

def entrance(s1, s2):
    def helper(i, j, substring):
        if i == 0 or j == 0:
            return substring[::-1] if substring.isupper() else ""
        if s1[i-1] == s2[j-1] and s1[i-1].isupper():
            return helper(i-1, j-1, substring + s1[i-1])
        else:
            return max(helper(i-1, j, ""), helper(i, j-1, ""), key=len)
    
    return helper(len(s1), len(s2), "")