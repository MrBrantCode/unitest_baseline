"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` that takes two strings `s1` and `s2` as input and returns the longest common substring between them. The substring should contain only alphabetic characters and should be case-sensitive. The function should have a time complexity of O(n^3), where n is the length of the longest string.
"""

def longest_common_substring(s1, s2):
    max_length = 0
    longest_substring = ""
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i].isalpha() and s2[j].isalpha() and s1[i] == s2[j]:
                current_length = 1
                substring = s1[i]
                k = 1
                
                while i+k < len(s1) and j+k < len(s2) and s1[i+k].isalpha() and s2[j+k].isalpha() and s1[i+k] == s2[j+k]:
                    substring += s1[i+k]
                    current_length += 1
                    k += 1
                
                if current_length > max_length:
                    max_length = current_length
                    longest_substring = substring
    
    return longest_substring