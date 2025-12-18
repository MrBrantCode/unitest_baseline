"""
QUESTION:
Design a function `countSubstrings(s)` that calculates the number of palindromic substrings in a given string `s`. The function should return the total count of palindromic substrings. The input string `s` consists of only lowercase English letters. The time complexity should be O(n^2) and space complexity should be O(n^2), where n is the length of the string `s`.
"""

def countSubstrings(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    count = 0

    for i in range(n):
        dp[i][i] = True
        count += 1

    for i in range(n-1, -1, -1): 
        for j in range(i+1, n):
            if s[i] == s[j]: 
                if j - i == 1 or dp[i+1][j-1]: 
                    dp[i][j] = True
                    count += 1

    return count