"""
QUESTION:
Given a string str of length n, find if the string is K-Palindrome or not. A k-palindrome string transforms into a palindrome on removing at most k characters from it.
Example 1:
Input: str = "abcdecba"
n = 8, k = 1
Output: 1
Explaination: By removing 'd' or 'e' 
we can make it a palindrome.
Example 2:
Input: str = "abcdefcba"
n = 9, k = 1
Output: 0
Explaination: By removing a single 
character we cannot make it a palindrome.
Your Task:
You do not need to read input or print anything. Your task is to complete the function kPalindrome() which takes string str, n and k as input parameters and returns 1 if str is a K-palindrome else returns 0.
Expected Time Complexity: O(n*n)
Expected Auxiliary Space: O(n*n)
Constraints:
1 ≤ n, k ≤ 10^{3}
"""

def is_k_palindrome(str, n, k):
    def isKPalDP(str1, str2, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if not i:
                    dp[i][j] = j
                elif not j:
                    dp[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
    
    rev = str[::-1]
    return 1 if isKPalDP(str, rev, n, n) <= 2 * k else 0