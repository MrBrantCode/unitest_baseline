"""
QUESTION:
Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:

Input: 5
Output: 5
Explanation: 
Here are the non-negative integers 


Note:
1 9
"""

def count_non_consecutive_binary_integers(n: int) -> int:
    dp = [1, 2]
    for i in range(2, 32):
        dp.append(dp[i - 1] + dp[i - 2])
    
    bnum = bin(n)[2:]
    size = len(bnum)
    ans = dp[size]
    
    for i in range(1, size):
        if bnum[i - 1] == bnum[i] == '1':
            break
        if bnum[i - 1] == bnum[i] == '0':
            ans -= dp[size - i] - dp[size - i - 1]
    
    return ans