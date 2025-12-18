"""
QUESTION:
Write a function `min_operations(string1, string2)` that calculates the minimum number of operations (insertions, deletions, and replacements) required to convert `string1` to `string2`. The function should return the minimum number of operations.
"""

def min_operations(string1, string2):
    m = len(string1)
    n = len(string2)

    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif string1[i - 1] == string2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                insert = table[i][j - 1] + 1
                delete = table[i - 1][j] + 1
                replace = table[i - 1][j - 1] + 1
                table[i][j] = min(insert, delete, replace)

    return table[m][n]