"""
QUESTION:
Given a row of n coins of values arr[1], arr[2], ... arr[n], where n is even. Geek plays a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount geek can get if he moves first.
Note: Both of them play optimally
Example 1:
Input: N = 4, arr[] = {5, 3, 7, 10}
Output: 15
Explanation: 
Geek chooses 10.
Opponent chooses 7.
Geek chooses 5.
Opponent chooses 3.
Example 2:
Input: N = 4, arr[] = {8, 15, 3, 7}
Output: 22
Explanation: 
Geek chooses 7.
Opponent chooses 8.
Geek chooses 15.
Opponent chooses 3.
Your Task:  
You don't need to read input or print anything. Complete the function maxAmount() which takes N  and array arr as input parameter and returns the maximum value geek can get.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
Constraints:
2 ≤ N ≤ 10^{3}
1 ≤ arr[i] ≤ 10^{5}
"""

def max_amount(arr, N):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = arr[i]
    
    for i in range(n - 1):
        dp[i][i + 1] = max(arr[i], arr[i + 1])
    
    for k in range(2, n):
        for i in range(n - k):
            j = i + k
            dp[i][j] = max(arr[i] + min(dp[i + 2][j], dp[i + 1][j - 1]), 
                           arr[j] + min(dp[i][j - 2], dp[i + 1][j - 1]))
    
    return dp[0][n - 1]