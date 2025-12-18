"""
QUESTION:
Create a function named `longest_subsequence` that takes a list of strings as input and returns the longest common subsequence among all the strings in the list. If the list is empty or there is no common subsequence, the function should return `None`. The subsequence does not need to be continuous in the given strings.
"""

from typing import List, Optional

def longest_subsequence(strings: List[str]) -> Optional[str]:
    def LCS(X , Y):
        m = len(X)
        n = len(Y)
        dp = [[None]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0 :
                    dp[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        index = dp[m][n]
        lcs = [""] * (index+1)
        lcs[index] = ""
        i = m
        j = n
        while i > 0 and j > 0:
            if X[i-1] == Y[j-1]:
                lcs[index-1] = X[i-1]
                i-=1
                j-=1
                index-=1
            elif dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1
        return "".join(lcs)
    
    if len(strings) == 0:
        return None
    lcs = strings[0]
    for string in strings[1:]:
        lcs = LCS(lcs, string)
        if not lcs:
            return None
    return lcs