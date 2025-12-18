"""
QUESTION:
Write a function called `lcs` that takes two strings `str1` and `str2` as input and returns their longest common subsequence. The function should not use any built-in sequence functions that can solve the problem directly.
"""

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    lcs = []
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs[::-1]