"""
QUESTION:
You are standing on a point (n, m) and you want to go to origin (0, 0) by taking steps either left or up i.e. from each point you are allowed to move either in (n-1, m) or (n, m-1). Find the number of paths from point to origin.
Example 1:
Input:
N=3, M=0
Output: 1
Explanation: Path used was - 
             (3,0)  --> ( 2,0) --> (1,0) --> (0,0).
             We can see that there is no other path
             other than this path for this testcase.
 
Example 2:
Input:
N=3, M=6
Output: 84 
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function ways() that takes array N and integer M as parameters and returns the total number of paths from point(n,m) to the origin(0,0) % 1000000007.
 
Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(N*M).
Constraints:
1 ≤ N, M ≤ 500
"""

def count_paths(n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 1
    
    # Initialize the DP table
    dp = [[1 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # Return the result modulo 1000000007
    return dp[n][m] % (10**9 + 7)