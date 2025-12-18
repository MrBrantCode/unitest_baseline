"""
QUESTION:
Write a function named `longest_symmetrical_subsequence` that takes a string `str` as input and returns the longest symmetrical subsequence in the string. The function should use dynamic programming to find the longest common subsequence between the original string and its reverse, and the time complexity should be O(n^2) where n is the length of the string.
"""

def longest_symmetrical_subsequence(str):
    str_rev = str[::-1]
    len_str = len(str)

    lcs_table = [[0 for x in range(len_str + 1)] for x in range(len_str + 1)]

    for i in range(len_str + 1):
        for j in range(len_str + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif str[i-1] == str_rev[j-1]:
                lcs_table[i][j] = lcs_table[i-1][j-1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])

    sym_subsequence = ""
    i = len_str
    j = len_str

    while i > 0 and j > 0:
        if str[i-1] == str_rev[j-1]:
            sym_subsequence += str[i-1]
            i -= 1
            j -= 1
        elif lcs_table[i-1][j] > lcs_table[i][j-1]:
            i -= 1
        else:
            j -= 1

    return sym_subsequence[::-1]