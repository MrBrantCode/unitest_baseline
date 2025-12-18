"""
QUESTION:
Create a function called `longestSubsequence` that takes two strings `x` and `y` as input. The function should find the longest common subsequence between `x` and `y`. The function should not use any built-in dynamic programming functions or libraries, and it should output the longest common subsequence.
"""

def longestSubsequence(x, y):
    m = len(x)
    n = len(y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    index = L[m][n]

    lcs = [""] * (index+1)
    lcs[index] = "\0"

    i = m
    j = n
    while i > 0 and j > 0:

        if x[i-1] == y[j-1]:
            lcs[index-1] = x[i-1]
            i-=1
            j-=1
            index-=1

        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1

    return "".join(lcs[:-1])