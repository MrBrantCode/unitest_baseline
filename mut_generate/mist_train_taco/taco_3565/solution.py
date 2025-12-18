"""
QUESTION:
Given an integer. Find how many structurally unique binary search trees are there that stores the values from 1 to that integer (inclusive). 
Example 1:
Input:
N = 2
Output: 2
Explanation:for N = 2, there are 2 unique
BSTs
     1               2  
      \            /
       2         1
Example 2:
Input:
N = 3
Output: 5
Explanation: for N = 3, there are 5
possible BSTs
  1           3     3       2     1
    \        /     /      /  \     \
     3      2     1      1    3     2
    /      /       \                 \
   2      1         2                 3
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numTrees() which takes the integer N as input and returns the total number of Binary Search Trees possible with keys [1.....N] inclusive. Since the answer can be very large, return the answer modulo 1e9 + 7.
Expected Time Complexity: O(N^{2}).
Expected Auxiliary Space: O(N).
Constraints:
1<=N<=1000
"""

def count_unique_bst(N: int) -> int:
    """
    Counts the number of structurally unique binary search trees that can be formed with nodes numbered from 1 to N.

    Parameters:
    N (int): The number of nodes in the binary search tree.

    Returns:
    int: The number of unique BSTs modulo 10^9 + 7.
    """
    if N == 0:
        return 1
    
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    MOD = 10 ** 9 + 7
    
    for i in range(2, N + 1):
        count = 0
        for j in range(1, i + 1):
            leftBST = dp[j - 1]
            rightBST = dp[i - j]
            count += leftBST * rightBST
        dp[i] = count % MOD
    
    return dp[N]