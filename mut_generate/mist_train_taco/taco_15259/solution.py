"""
QUESTION:
Geek wants to distribute M balls among N children. His nemesis Keeg wants to disrupt his plan and removes P balls from Geek's bag. The minimum number of balls required to make each child happy are given in an array arr[]. Find the number of ways Geek can distribute the remaining balls so that each is happy. 
Example 1:
Input: 
m = 13, n = 4, p = 5
arr = {2, 3, 1, 3}
Output: -1
Explaination: Number of balls left is 
m-p = 8. Minimum 9 balls are required to 
make everyone happy. So the task is not 
possible and the answer is -1.
Example 2:
Input: 
m = 30, n = 10, p = 14
arr = {2, 2, 1, 1, 1, 2, 2, 3, 1, 1}
Output: 1
Explaination: At least 16 balls are required 
to make the children happy. 16 balls are left. 
So there is only one way to make them happy.
Your Task:
You do not need to read input or print anything. Your task is to complete the function countWays() which takes m, n, p and arr as input parameters and returns the  number of possible ways to distribute the balls. Return the answer modulo 10^{9} + 7. If there is no way of making everyone happy, return -1.
Expected Time Complexity: O(m*n)
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ m, p ≤ 1000
1 ≤ n ≤ 100
1 < arr[i] < 10
"""

def count_ways_to_distribute_balls(m, n, p, arr):
    # Calculate the remaining number of balls after removal
    remaining_balls = m - p
    
    # Check if the remaining balls are sufficient to make all children happy
    if sum(arr) > remaining_balls:
        return -1
    
    # Modulo value for the result
    mod = 1000000007
    
    # Initialize the DP table
    dp = [[0 for _ in range(remaining_balls + 1)] for _ in range(n)]
    
    # Fill the DP table
    for i in range(1, remaining_balls + 1):
        dp[0][i] = 1 if i >= arr[0] else 0
    
    for i in range(1, n):
        for j in range(remaining_balls + 1):
            if j >= arr[i]:
                dp[i][j] = dp[i - 1][j - arr[i]] + dp[i][j - 1]
            dp[i][j] = dp[i][j] % mod
    
    return dp[n - 1][remaining_balls]