"""
QUESTION:
Given two string X and Y of length N and M respectively. The task is to find the length of the longest subsequence of string X which is a substring in sequence Y.
Example 1:
Input:
N = 4, M = 8
X = "abcd"
Y = "bacdbdcd"
Output: 3
Explanation: "acd" is the longest subsequence
             from string X present as a
             substring in string Y.
Example 2:
Input:
N = 1, M = 1
X = 'a'
Y = 'a'
Output: 1
Explanation: 'a' is the answer.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxSubsequenceSubstring() which takes 4 arguments(string X, string Y, N and M) and returns the answer. 
Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(N*M).
Constraints:
1<= N, M <=10^{3}
"""

def max_subsequence_substring(X: str, Y: str, N: int, M: int) -> int:
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    res = 0
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                res = max(res, dp[i][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return res