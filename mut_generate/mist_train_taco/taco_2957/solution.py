"""
QUESTION:
Given an array arr[] of N elements. Find the number of non-empty subsets whose product of elements is less than or equal to a given integer K. 
 
Example 1:
Input:
N = 4
arr[] = {2, 4, 5, 3}
K = 12
Output:
8
Explanation:
All possible subsets whose 
products are less than 12 are:
(2), (4), (5), (3), (2, 4), (2, 5), (2, 3), (4, 3)
Example 2:
Input:
N = 3
arr[] = {9, 8, 3}
K = 2 
Output:
0
Explanation:
There is no subsets with product less
than or equal to 2.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function numOfSubsets() which takes 2 integers N, and K, and an array arr of size N as input and returns the number of subsets with product less equal to K.
Expected Time Complexity: O(N*2^{N/2})
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 30
1 ≤ arr[i] ≤ 10
1 ≤ K ≤ 10^{6}
"""

def count_subsets_with_product_less_than_or_equal_to_k(arr, k):
    def f(arr, i, k, dp):
        if i < 0:
            if k > 0:
                return 1
            else:
                return 0
        if dp[i][k] != -1:
            return dp[i][k]
        nt = f(arr, i - 1, k, dp)
        t = 0
        if arr[i] <= k:
            t = f(arr, i - 1, k // arr[i], dp)
        dp[i][k] = t + nt
        return dp[i][k]

    n = len(arr)
    dp = [[-1] * (k + 1) for _ in range(n + 1)]
    return f(arr, n - 1, k, dp) - 1