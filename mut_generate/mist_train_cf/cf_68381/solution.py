"""
QUESTION:
Write a function `longestLine(M)` that takes a binary matrix `M` as input and returns a tuple containing the length of the longest line of consecutive ones in the matrix and a list of the starting and ending coordinates of the line. The line could be horizontal, vertical, diagonal, or anti-diagonal. The function should handle cases where the matrix is empty. The matrix contains at most 10,000 elements. The function should return the starting and ending coordinates of the longest line of consecutive ones.
"""

def entance(M):
    if not M: return 0, []
    n, m = len(M), len(M[0])
    up = [[0]*m for _ in range(n)]
    left = [[0]*m for _ in range(n)]
    diag = [[0]*m for _ in range(n)]
    anti = [[0]*m for _ in range(n)]
    maxLen = 0
    maxLine = []

    for i in range(n):
        for j in range(m):
            if M[i][j] == 1:
                up[i][j] = (up[i-1][j] if i > 0 else 0) + 1
                left[i][j] = (left[i][j-1] if j > 0 else 0) + 1
                diag[i][j] = (diag[i-1][j-1] if i > 0 and j > 0 else 0) + 1
                anti[i][j] = (anti[i-1][j+1] if i > 0 and j < m - 1 else 0) + 1
                maxLineLen = max(up[i][j], left[i][j], diag[i][j], anti[i][j])
                if maxLineLen > maxLen:
                    maxLen = maxLineLen
                    if maxLineLen == up[i][j]:
                        maxLine = [(i - maxLen + 1, j), (i, j)]
                    elif maxLineLen == left[i][j]:
                        maxLine = [(i, j - maxLen + 1), (i, j)]
                    elif maxLineLen == diag[i][j]:
                        maxLine = [(i - maxLen + 1, j - maxLen + 1), (i, j)]
                    elif maxLineLen == anti[i][j]:
                        maxLine = [(i - maxLen + 1, j + maxLen - 1), (i, j)]

    return maxLen, maxLine