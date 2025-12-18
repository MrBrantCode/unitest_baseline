"""
QUESTION:
Implement a function called "longest_common_substring" that takes two strings s1 and s2 as input and returns the longest common substring found between them, case-insensitive. The function should consider all possible substrings of both strings and return the longest one that appears in both strings. If there are multiple substrings with the same length, return the one that appears first in the first string. Assume the input strings only contain alphanumeric characters and spaces, with no leading or trailing spaces, and may have different lengths.
"""

def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)

    # Initialize matrix
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to track longest substring
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1].lower() == s2[j - 1].lower():
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_index = i

    # Extract longest common substring from s1
    longest_substring = s1[end_index - max_length: end_index]

    return longest_substring