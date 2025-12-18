"""
QUESTION:
The task is to count all the possible paths from top left to bottom right of a m X n matrix with the constraints that from each cell you can either move only to right or down.
Example 1:
Input: m = 2, n = 2
Output: 2 
Explanation: Two possible ways are
RD and DR.  
Example 2:
Input: m = 3, n = 3
Output: 6
Explanation: Six possible ways are
RRDD, DDRR, RDDR, DRRD, RDRD, DRDR. 
Your Task:  
You dont need to read input or print anything. Complete the function numberOfPaths() which takes m and n as input parameter and returns count all the possible paths.The answer may be very large, compute the answer modulo 10^{9} + 7.
Expected Time Complexity: O(m*n)
Expected Auxiliary Space: O(m*n)
Constraints:
1 <= m <=100
1 <= n <=100
"""

def count_paths(m: int, n: int) -> int:
    def fin(x: int, y: int, m: int, n: int, dp: list) -> int:
        if x >= n or y >= m:
            return 0
        if x == n - 1 and y == m - 1:
            return 1
        if dp[x][y] != -1:
            return dp[x][y]
        else:
            dp[x][y] = (fin(x + 1, y, m, n, dp) + fin(x, y + 1, m, n, dp)) % (10**9 + 7)
            return dp[x][y]

    dp = [[-1 for _ in range(m)] for _ in range(n)]
    return fin(0, 0, m, n, dp)