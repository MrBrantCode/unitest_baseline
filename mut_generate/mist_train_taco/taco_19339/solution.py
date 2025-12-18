"""
QUESTION:
Given two integers N and K, the task is to find the count of palindromic strings of length lesser than or equal to N, with first K characters of lowercase English language, such that each character in a string doesn’t appear more than twice.
Note: Anwer can be very large, so, output answer modulo 10^{9}+7
Example 1:
Input: N = 3, K = 2
Output: 6
Explanation: The possible strings are:
"a", "b", "aa", "bb", "aba", "bab".
Example 2:
Input: N = 4, K = 3
Output: 18
Explanation: The possible strings are: 
"a", "b", "c", "aa", "bb", "cc", "aba",
"aca", "bab", "bcb", "cac", "cbc", 
"abba", "acca", "baab", "bccb", "caac", 
"cbbc". 
Your task:
You do not need to read any input or print anything. The task is to complete the function palindromicStrings(), which takes two integers as input and returns the count. 
Expected Time Complexity: O(K^{2})
Expected Auxiliary Space: O(K^{2})
Constraints:
1 ≤ K ≤ 26
1 ≤ N ≤ 52
N ≤ 2*K
"""

def count_palindromic_strings(N: int, K: int) -> int:
    mod = 1000000007
    
    def rec(N, K, dp):
        if N == 0:
            return 1
        if K == 0:
            return 0
        if N == 1:
            return K
        if dp[N][K] != -1:
            return dp[N][K]
        dp[N][K] = rec(N - 2, K - 1, dp) * K
        return dp[N][K]
    
    dp = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]
    count = 0
    for i in range(1, N + 1):
        count += rec(i, K, dp)
    return count % mod