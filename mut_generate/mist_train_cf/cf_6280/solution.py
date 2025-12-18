"""
QUESTION:
Write a function `longest_common_substring(list1, list2)` that finds the longest common substring between two lists of strings, considering only substrings of length greater than or equal to 6 characters. If there are multiple common substrings of the same length, return the one that appears last in the second list. The function should return `None` if no common substring of length 6 or greater is found.
"""

def longest_common_substring(list1, list2):
    longest_substring = ''
    for word1 in list1:
        for word2 in list2:
            for i in range(len(word2) - 5):
                substring = word2[i:i+6]
                if substring in word1 and len(substring) > len(longest_substring):
                    longest_substring = substring
            # Check the remaining part of the word2
            for j in range(6, len(word2)):
                substring = word2[j:]
                if substring in word1 and len(substring) > len(longest_substring):
                    longest_substring = substring
    return longest_substring