"""
QUESTION:
Given a string s, determine if it contains any palindrome of length exactly 100 as a subsequence. If it has any, print any one of them. If it doesn't have any, print a palindrome that is a subsequence of s and is as long as possible.

Input

The only line of the input contains one string s of length n (1 ≤ n ≤ 5·104) containing only lowercase English letters.

Output

If s contains a palindrome of length exactly 100 as a subsequence, print any palindrome of length 100 which is a subsequence of s. If s doesn't contain any palindromes of length exactly 100, print a palindrome that is a subsequence of s and is as long as possible.

If there exists multiple answers, you are allowed to print any of them.

Examples

Input

bbbabcbbb


Output

bbbcbbb


Input

rquwmzexectvnbanemsmdufrg


Output

rumenanemur

Note

A subsequence of a string is a string that can be derived from it by deleting some characters without changing the order of the remaining characters. A palindrome is a string that reads the same forward or backward.
"""

def find_palindrome_subsequence(s: str) -> str:
    n = len(s)
    last = [[0] * 26 for _ in range(n)]
    last[0][ord(s[0]) - 97] = 0
    
    for i in range(1, n):
        for j in range(26):
            last[i][j] = last[i - 1][j]
        last[i][ord(s[i]) - 97] = i
    
    dp = [''] * n
    
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            k = last[j][ord(s[i]) - 97]
            if k > i:
                if k - i == 1 and len(dp[j]) < 2:
                    dp[j] = s[i] + s[i]
                elif len(dp[j]) < len(dp[k - 1]) + 2:
                    dp[j] = s[i] + dp[k - 1] + s[i]
                    if len(dp[j]) >= 100:
                        if len(dp[j]) == 101:
                            return dp[j][:50] + dp[j][51:]
                        else:
                            return dp[j]
        dp[i] = s[i]
    
    return dp[n - 1]