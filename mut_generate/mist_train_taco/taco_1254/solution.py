"""
QUESTION:
Given string s consisting of digits 0-9 and a number N, the task is to count the number of subsequences that are divisible by N.
Note: Answer can be large, output answer modulo 10^{9} + 7
Example 1:
Input: s = "1234", N = 4
Output: 4
Explanation: The subsequences 4, 12, 24 and 
124 are divisible by 4.
Example 2:
Input: s = "330", N = 6
Output: 4
Explanation: The subsequences 30, 30, 330 
and 0 are divisible by 6.
Your Task:  
You don't need to read input or print anything. Complete the function countDivisibleSubseq() which takes s and N as input parameters and returns the integer value
Expected Time Complexity: O(|s|*N)
Expected Auxiliary Space: O(|s|*N)
Constraints:
1 ≤ |s|*N ≤ 10^{6}
"""

def count_divisible_subseq(s: str, N: int) -> int:
    mod = 1000000007
    l = len(s)
    dp = [[0 for _ in range(l)] for _ in range(N)]
    
    # Initialize the first character
    dp[int(s[0]) % N][0] += 1
    
    # Fill the DP table
    for i in range(1, l):
        dp[int(s[i]) % N][i] += 1
        for j in range(N):
            dp[j][i] += dp[j][i - 1]
            dp[(j * 10 + int(s[i])) % N][i] += dp[j][i - 1]
    
    # The answer is the number of subsequences ending at the last character that are divisible by N
    return dp[0][l - 1] % mod