"""
QUESTION:
Given a floor of size n x m and tiles of size 1 x m. The problem is to count the number of ways to tile the given floor using 1 x m tiles. A tile can either be placed horizontally or vertically.
Both n and m are positive integers and 2 < = m.
 
Example 1 :
Input: n = 2, m = 3
Output: 1
Expanation: There is only one way to tile the
given floor.
Example 2 :
Input: n = 4, m = 4
Output: 2
Explanation: There is two ways to tile the
given floor.One way is to place 1 x 4 size 
of tile vertically and another one is to 
place them horizontally.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function countWays() which takes n and m as input parameter and returns the total ways modulo 10^{9} + 7.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
 
Constraints:
1 <= n <= 100000
2 <= m <= 100000
"""

def count_ways_to_tile(n: int, m: int) -> int:
    MOD = 1000000007
    dp = [0] * (n + 1)
    
    for i in range(n + 1):
        if i < m:
            dp[i] = 1
        elif i == m:
            dp[i] = 2
        else:
            dp[i] = (dp[i - 1] + dp[i - m]) % MOD
    
    return dp[n]