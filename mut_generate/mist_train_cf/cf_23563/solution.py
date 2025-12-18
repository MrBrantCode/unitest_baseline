"""
QUESTION:
Construct a function `longest_common_subsequence(s1, s2)` that takes two string parameters `s1` and `s2` and returns the longest common subsequence between the two strings. The function should not use any built-in functions that directly solve the problem. The function should be able to handle strings of any length.
"""

def entrance(s1, s2):
    num_rows = len(s1) + 1
    num_cols = len(s2) + 1
    matrix = [[0 for x in range(num_cols)] for y in range(num_rows)]

    for r in range(1, num_rows):
        for c in range(1, num_cols):
            if s1[r-1] == s2[c-1]:
                matrix[r][c] = matrix[r-1][c-1] + 1
            else:
                matrix[r][c] = max(matrix[r-1][c], matrix[r][c-1])

    result = ""
    r = num_rows - 1
    c = num_cols - 1
    while r > 0 and c > 0:
        if s1[r-1] == s2[c-1]:
            result = s1[r-1] + result
            r -= 1
            c -= 1
        elif matrix[r-1][c] > matrix[r][c-1]:
            r -= 1
        else:
            c -= 1
    return result