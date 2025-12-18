"""
QUESTION:
Given a string str of length N, you have to find number of palindromic subsequence (need not necessarily be distinct) present in the string str.
Note: You have to return the answer module 10^{9}+7;
 
Example 1:
Input: 
Str = "abcd"
Output: 
4
Explanation:
palindromic subsequence are : "a" ,"b", "c" ,"d"
 
Example 2:
Input: 
Str = "aab"
Output: 
4
Explanation:
palindromic subsequence are :"a", "a", "b", "aa"
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countPs() which takes a string str as input parameter and returns the number of palindromic subsequence.
 
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N*N)
Constraints:
1<=length of string str <=1000
"""

def count_palindromic_subsequences(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
    
    # Return the result modulo 10^9 + 7
    return dp[0][n - 1] % (10**9 + 7)