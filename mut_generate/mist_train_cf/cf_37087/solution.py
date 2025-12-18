"""
QUESTION:
Write a function `longestCommonSubstring(a, b)` that finds the length of the longest common substring between two given strings `a` and `b`. The input strings will only contain lowercase letters.
"""

def longestCommonSubstring(a, b):
    matrix = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    max_length = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                max_length = max(max_length, matrix[i][j])
    return max_length