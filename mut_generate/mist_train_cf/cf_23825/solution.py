"""
QUESTION:
Write a function `longest_common_subsequence(str1, str2)` that takes two input strings and returns their longest common subsequence. The longest common subsequence is a sequence that appears in the same relative order in both strings, but may not be contiguous. The function should not use any built-in sequence alignment functions.
"""

def entance(str1, str2):
    m = len(str1)
    n = len(str2)

    matrix = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    result = ""
    i = m
    j = n

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            result += str1[i-1]
            i -= 1
            j -= 1

        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return result[::-1]