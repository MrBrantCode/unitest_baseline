"""
QUESTION:
Given two integers n and k, count the number of binary strings of length n where adjacent 1 appear k times. Since the answer can be huge, print it modulo 10^{9}+7.
Example 1:
Input:
n = 3 , k = 2
Output: 1
Explanation: Possible string is "111".
Example 2:
Input:
n = 5 , k = 2
Output: 6
Explanation: Possible strings are:
"00111" , "10111" , "01110"
"11100" , "11101" , "11011".
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countStrings() which accepts integers n and k as input parameter and returns the number of binary strings that satisfy the given condition.
Expected Time Complexity: O(n*k).
Expected Auxiliary Space: O(n*k). 
Constraints:
1 <= n, k <= 10^{3}
"""

def count_binary_strings(n: int, k: int) -> int:
    MOD = 1000000007
    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
    dp[1][0][0] = 1
    dp[1][0][1] = 1
    
    for i in range(2, n + 1):
        for j in range(k + 1):
            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
            dp[i][j][1] = dp[i - 1][j][0]
            if j >= 1:
                dp[i][j][1] = (dp[i][j][1] + dp[i - 1][j - 1][1]) % MOD
    
    return (dp[n][k][0] + dp[n][k][1]) % MOD