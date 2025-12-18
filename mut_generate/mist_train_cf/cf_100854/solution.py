"""
QUESTION:
Write a function `longest_common_subsequence(str1, str2)` that takes two strings as input and returns the longest common subsequence of the two strings. The function should have a time complexity of O(mn), where m and n are the lengths of the input strings.
"""

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    lcs = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    index = lcs[m][n]
    lcs_str = [""] * (index+1)
    lcs_str[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_str[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs[i-1][j] > lcs[i][j-1]:
            i -= 1
        else:
            j -= 1
    return "".join(lcs_str)