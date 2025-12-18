"""
QUESTION:
Given two numbers M and N, which represents the length and breadth of a paper, the task is to cut the paper into squares of any size and find the minimum number of squares that can be cut from the paper.
Example 1:
Input: M = 36, N = 30
Output: 5
Explanation: 
3 (squares of size 12x12) + 
2 (squares of size 18x18)
Example 2:
Input: M = 4, N = 5
Output: 5
Explanation: 
1 (squares of size 4x4) + 
4 (squares of size 1x1)
Your Task:  
You don't need to read input or print anything. Complete the function minCut() which takes M and N as input parameters and returns the integer value
Expected Time Complexity: O(M*N*(N +M))
Expected Auxiliary Space: O(M*N)
Constraints:
1 ≤ M, N ≤ 10^{2}
"""

def min_squares_cut(M, N):
    def get(m, n, dp):
        if m == n:
            return 1
        if dp[m][n] != -1:
            return dp[m][n]
        ans = sys.maxsize
        for i in range(1, m // 2 + 1):
            ans = min(ans, get(i, n, dp) + get(m - i, n, dp))
        for i in range(1, n // 2 + 1):
            ans = min(ans, get(m, i, dp) + get(m, n - i, dp))
        dp[m][n] = ans
        return dp[m][n]

    import sys
    dp = []
    for i in range(0, M + 1):
        dp.append([-1] * (N + 1))
    return get(M, N, dp)