"""
QUESTION:
Find the number of ways in which N coins can be distributed among K pupils such that each pupil receives at least one coin each. Two distributions are said to be different only if they have at least one pupil who got a different number of coins.
 
Example 1:
Input: N = 7, K = 3
Output: 15
Explanation: 
Coin distribution can be any of the following 15 ways. 
{1,1,5}, {1,5,1}, {5,1,1}, {2,1,4}, {1,2,4}, {1,4,2}
{2,4,1}, {4,1,2}, {4,2,1}, {3,1,3}, {1,3,3}, {3,3,1}
{2,2,3}, {2,3,2}, {3,2,2}
Example 2:
Input: N = 5, K = 5
Output: 1
Explanation: {1, 1, 1, 1, 1} is the only way.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function totalWays() which takes N and K as input parameters and returns the number of possible distributions modulo 10^9+7.
 
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
 
Constraints:
1 <= N, K <= 100000
"""

import math

def total_ways(N, K):
    MOD = 1000000007
    
    if N < K:
        return 0
    
    # Calculate the denominator
    den = math.factorial(K - 1) * math.factorial(N - K)
    
    # Calculate the numerator
    num = math.factorial(N - 1)
    
    # Calculate the result
    ans = num // den
    
    return ans % MOD