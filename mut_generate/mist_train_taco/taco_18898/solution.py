"""
QUESTION:
You are provided an input string S and the string “GEEKS” . Find the number of ways in which the subsequence “GEEKS” can be formed from the string S.
 
Example 1:
Input : S = "GEEKS"
Output: 1
Explanation: 
"GEEKS" occurs in S only once.
Example 2:
Input: S = "AGEEKKSB"
Output: 2
Explanation: Subsequenece "GEEKS" occurs in 
S two times. First one is taking the first 
'K' into consideration and second one is 
taking second 'K'.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function TotalWays() which takes string S as input paramater and returns total ways modulo 10^{9} + 7.
 
Expected Time Complexity : O(N * K) where N is length of string and K is constant.
Expected Space Complexity: O(N * K)
 
Constraints: 
1 <= Length od string <= 10000
"""

def count_subsequence_ways(s1: str) -> int:
    mod = 1000000007
    s2 = 'GEEKS'
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    dp[0][0] = 1
    
    for i in range(1, len(s1) + 1):
        dp[i][0] = 1
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[len(s1)][len(s2)]