"""
QUESTION:
You are given N balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array arr. You are asked to burst all the balloons.
If you burst the ith balloon, you will get arr[ i - 1 ] * arr[ i ] * arr[ i + 1] coins. If i - 1, or i + 1 goes out of the bounds of the array, consider it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.
Example 1:
Input:
N = 4
arr[ ] = {3, 1, 5, 8}
Output: 167
Explanation: 
arr[ ] = {3, 1, 5, 8}  - - > {3, 5, 8} - - > {3, 8} - - > { 8} - -> { }
coins = 3 *1 *5,      +      3*5*8     +   1*3*8   +  1*8*1   = 167
 
 
Example 2:
Input:
N = 2
arr[ ] = {1, 10}
Output: 20
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxCoins() which takes the array of integers arr and N as parameters and returns the maximum coin you can collect.
Expected Time Complexity: O(N*N*N)
Expected Auxiliary Space: O(N*N)
Constraints:
1 ≤ N ≤ 300
0 ≤ arr [ i ]  ≤ 100
"""

from typing import List
import sys

def max_coins(arr: List[int], N: int) -> int:
    # Insert 1 at the beginning and end of the array to handle boundary conditions
    arr.insert(0, 1)
    arr.append(1)
    
    # Initialize the DP table
    dp = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
    
    # Fill the DP table
    for i in range(N, 0, -1):
        for j in range(1, N + 1):
            if i > j:
                continue
            maxi = -sys.maxsize - 1
            for ind in range(i, j + 1):
                cost = arr[i - 1] * arr[ind] * arr[j + 1] + dp[i][ind - 1] + dp[ind + 1][j]
                maxi = max(maxi, cost)
                dp[i][j] = maxi
    
    # The result is stored in dp[1][N]
    return dp[1][N]