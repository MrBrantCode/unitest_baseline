"""
QUESTION:
You are given two arrays A and B of integers, where the integers in each array are distinct. Draw connecting lines between the integers in A and B such that each line does not intersect with any other connecting line and A[i] == B[j]. Determine and return the maximum quantity of connecting lines that can be drawn. 

Function: maxUncrossedLines(A, B)

Constraints: 
1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
"""

def maxUncrossedLines(A, B):
    M, N = len(A), len(B)
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a == b:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[-1][-1]