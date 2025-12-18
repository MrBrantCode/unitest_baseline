"""
QUESTION:
Write a function named `longest_common_substring` that takes two parameters: `string1` and `string2`, which are the input strings to find the longest common substring. The function should return the longest common substring. The function should be able to handle strings of any length and any characters. The solution can use any algorithm, but it should be efficient for large strings.
"""

def longest_common_substring(string1, string2):
    m = len(string1)
    n = len(string2)

    lengths = [[0] * (n+1) for i in range(m+1)]
    longest = 0
    x_longest = 0

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lengths[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                lengths[i][j] = lengths[i-1][j-1] + 1
                if lengths[i][j] > longest:
                    longest = lengths[i][j]
                    x_longest = i
            else:
                lengths[i][j] = 0

    return string1[x_longest - longest: x_longest]