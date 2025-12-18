"""
QUESTION:
Write a function named `longest_common_substring` that takes two lists of strings as input and returns the longest common substring of length 6 or greater. If there are multiple common substrings of the same length, return the one that appears last in the second list. If no common substring of length 6 or greater is found, return None.
"""

def longest_common_substring(list1, list2):
    longest_substring = ''
    for word1 in list1:
        for word2 in list2:
            for i in range(len(word2) - 5):
                substring = word2[i:i+6]
                if substring in word1 and len(substring) > len(longest_substring):
                    longest_substring = substring
                for j in range(7, len(word2) - i + 1):
                    substring = word2[i:i+j]
                    if substring in word1 and len(substring) > len(longest_substring):
                        longest_substring = substring
    return longest_substring