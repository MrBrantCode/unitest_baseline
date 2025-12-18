"""
QUESTION:
Write a function `longest_common_substring(str1, str2)` that returns the length of the longest common substring between two input strings `str1` and `str2`. The function should be case-sensitive and consider substrings of any length that appear consecutively in both strings. If there are multiple common substrings of the same maximum length, return the length of the first one encountered. The input strings can have a maximum length of 10^5 characters each and may contain any printable ASCII characters.
"""

def longest_common_substring(str1, str2):
    max_len = 0
    len1 = len(str1)
    len2 = len(str2)

    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                curr_len = 1
                k = 1
                while (i+k) < len1 and (j+k) < len2 and str1[i+k] == str2[j+k]:
                    curr_len += 1
                    k += 1
                if curr_len > max_len:
                    max_len = curr_len

    return max_len