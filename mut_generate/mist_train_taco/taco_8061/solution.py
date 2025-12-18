"""
QUESTION:
Given a parent array arr[] of a binary tree of N nodes. Element at index i in the array arr[] represents the parent of ith node, i.e, arr[i] = parent(i). Find the height of this binary tree.
Note: There will be a node in the array arr[], where arr[i] = -1, which means this node is the root of binary tree.
Example 1:
Input: N = 7
arr = {-1, 0, 0, 1, 1, 3, 5}
Output: 5
Explanation: Tree formed is:
                    0
                   / \
                  1   2
                 / \
                3   4
               /
              5
             /
            6      Height of the tree= 5
Your Task:
You do not need to read input or print anything. Your task is to complete the function findHeight() which takes N and arr[] as input parameters and returns the height of the given binary tree.
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ arr[i] ≤ 105
"""

def find_binary_tree_height(N, arr):
    def solve(arr, i, dp):
        if arr[i] == -1:
            return 1
        if dp[i] != -1:
            return dp[i]
        dp[i] = solve(arr, arr[i], dp) + 1
        return dp[i]

    dp = [-1] * N
    max_height = 0
    for i in range(N):
        max_height = max(max_height, solve(arr, i, dp))
    return max_height