"""
QUESTION:
Given a String, find the longest palindromic subsequence.
Example 1:
Input:
S = "bbabcbcab"
Output: 7
Explanation: Subsequence "babcbab" is the
longest subsequence which is also a palindrome.
Example 2:
Input: 
S = "abcd"
Output: 1
Explanation: "a", "b", "c" and "d" are
palindromic and all have a length 1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestPalinSubseq() which takes the string S as input and returns an integer denoting the length of the longest palindromic subsequence of S.
Expected Time Complexity: O(|S|*|S|).
Expected Auxiliary Space: O(|S|*|S|).
Constraints:
1 ≤ |S| ≤ 1000
"""

def longest_palindromic_subsequence(s: str) -> int:
    rs = s[::-1]
    n = len(s)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rs[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][n]