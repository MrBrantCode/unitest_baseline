"""
QUESTION:
Write a function `find_longest_common_substring` that takes two lists of strings as input and returns the longest common substring of length at least 4 characters. If there are multiple common substrings of the same length, return the one that appears first in the first list. If no common substring is found, return None.
"""

def find_longest_common_substring(list1, list2):
    longest_substring = ""
    
    for word1 in list1:
        for word2 in list2:
            for i in range(len(word1) - 3):
                for j in range(i + 4, len(word1) + 1):
                    substring = word1[i:j]
                    if substring in word2 and len(substring) > len(longest_substring):
                        longest_substring = substring
                        
    if len(longest_substring) > 0:
        return longest_substring
    else:
        return None