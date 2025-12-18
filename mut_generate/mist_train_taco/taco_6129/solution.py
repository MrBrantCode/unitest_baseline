"""
QUESTION:
In the stock market, a person buys a stock and sells it on some future date. Given the stock prices of N days in an array A[ ] and a positive integer K, find out the maximum profit a person can make in at-most K transactions. A transaction is equivalent to (buying + selling) of a stock and new transaction can start only when the previous transaction has been completed.
Example 1:
Input: K = 2, N = 6
A = {10, 22, 5, 75, 65, 80}
Output: 87
Explaination: 
1st transaction: buy at 10 and sell at 22. 
2nd transaction : buy at 5 and sell at 80.
Example 2:
Input: K = 3, N = 4
A = {20, 580, 420, 900}
Output: 1040
Explaination: The trader can make at most 2 
transactions and giving him a profit of 1040.
Example 3:
Input: K = 1, N = 5
A = {100, 90, 80, 50, 25}
Output: 0
Explaination: Selling price is decreasing 
daily. So seller cannot have profit.
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxProfit() which takes the values K, N and the array A[] as input parameters and returns the maximum profit.
Expected Time Complexity: O(N*K)
Expected Auxiliary Space: O(N*K)
Constraints:
1 ≤ N ≤ 500
1 ≤ K ≤ 200
1 ≤ A[ i ] ≤ 1000
"""

def max_profit(K, N, A):
    if K == 0 or N == 0:
        return 0
    
    # Initialize a 3D DP array with dimensions [N][K+1][2]
    dp = [[[0 for _ in range(2)] for _ in range(K + 1)] for _ in range(N)]
    
    # Base cases
    for i in range(N):
        dp[i][0][0] = 0  # No transactions, no profit
    
    for k in range(K + 1):
        dp[0][k][0] = 0  # No profit on the first day if no stock is bought
        dp[0][k][1] = -A[0]  # Buying stock on the first day
    
    # Fill the DP table
    for i in range(1, N):
        for k in range(1, K + 1):
            dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + A[i])
            dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - A[i])
    
    # The maximum profit will be in dp[N-1][K][0]
    return dp[N - 1][K][0]