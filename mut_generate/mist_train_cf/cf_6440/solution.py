"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` that finds the longest common substring from two given strings `s1` and `s2`. The function should handle case-sensitive strings that can contain special characters and should not use any built-in functions or libraries specifically designed for string manipulation. The time complexity of the function should be O(n^4), where n is the length of the longer string, and the space complexity should be O(1).
"""

def longest_common_substring(s1, s2):
    longestSubstring = ""
    for i in range(len(s1)):
        for j in range(len(s2)):
            currentSubstring = ""
            k, col = i, j
            while k < len(s1) and col < len(s2) and s1[k] == s2[col]:
                currentSubstring += s1[k]
                k += 1
                col += 1
            if len(currentSubstring) > len(longestSubstring):
                longestSubstring = currentSubstring
    return longestSubstring