"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` that takes two strings `s1` and `s2` as input and returns the longest common substring between them. The function should be able to handle strings containing uppercase and lowercase letters, numbers, and special characters.
"""

def entance(s1, s2):
    table = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_length = 0
    ending_pos = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    ending_pos = i
            else:
                table[i][j] = 0
    longest_substring = s1[ending_pos - max_length:ending_pos]
    return longest_substring