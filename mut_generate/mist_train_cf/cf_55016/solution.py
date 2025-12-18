"""
QUESTION:
Write a function `findLongest(s1, s2, s3)` that takes three strings `s1`, `s2`, and `s3` as input and returns the length of the longest common subsequence among these three strings. The function should use dynamic programming and the input strings can be of any length.
"""

def findLongest(s1, s2, s3):
    # Memoization storage
    len1, len2, len3 = len(s1), len(s2), len(s3)
    t = [[[0 for k in range(len3+1)] for j in range(len2+1)]
        for i in range(len1+1)]
 
    # Fill the storage
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            for k in range(len3 + 1):
                if (i == 0 or j == 0 or k == 0):
                    t[i][j][k] = 0
                elif (s1[i - 1] == s2[j - 1] and s2[j - 1] == s3[k - 1]):
                    t[i][j][k] = t[i - 1][j - 1][k - 1] + 1
                else:
                    t[i][j][k] = max(max(t[i - 1][j][k],
                        t[i][j - 1][k]),
                        t[i][j][k - 1])
    return t[len1][len2][len3]