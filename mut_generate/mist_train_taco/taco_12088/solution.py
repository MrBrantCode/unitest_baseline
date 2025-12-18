"""
QUESTION:
Given a rope of length N meters, cut the rope into several ropes of varying lengths in a way that maximizes product of lengths of all resulting ropes. You must make at least one cut.
Example 1:
Input:
N = 2
Output: 1
Explanation: Since 1 cut is mandatory.
Maximum obtainable product is 1*1 = 1.
Example 2:
Input:
N = 5
Output: 6
Explanation: 
Maximum obtainable product is 2*3 = 6.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxProduct() which takes n as input parameter and returns the maximum product.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 100
"""

def max_product_of_rope_cuts(n: int) -> int:
    if n <= 1:
        return 0  # Edge case: no cuts can be made for ropes of length 1 or less
    
    dp = [0] * (n + 1)
    dp[1] = 0  # Base case: no cuts can be made for a rope of length 1
    
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    
    return dp[n]