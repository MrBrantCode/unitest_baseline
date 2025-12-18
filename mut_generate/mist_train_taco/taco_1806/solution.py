"""
QUESTION:
Given a preorder traversal of a BST, find the leaf nodes of the tree without building the tree.
Example 1:
Input:
N = 2
arr = {2,1}
Output: {1}
Explaination: 1 is the only leaf node.
Example 2:
Input:
N = 3
Arr = {3, 2, 4}
Output: {2, 4}
Explaination: 2, 4 are the leaf nodes.
Your Task:
You don't need to read input or print anything. Your task is to complete the function leafNodes() which takes the array arr[] and its size N as input parameters and returns the leaf nodes of the tree.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{3}
1 ≤ arr[i] ≤ 10^{3}
"""

def find_leaf_nodes(arr, N):
    def leaf_nodes_helper(arr, N, ans):
        if N == 0:
            return
        if N == 1:
            ans.append(arr[0])
            return
        root = arr[0]
        index = 1
        for i in range(1, N):
            if arr[0] < arr[i]:
                index = i
                break
        leaf_nodes_helper(arr[1:index], len(arr[1:index]), ans)
        leaf_nodes_helper(arr[index:], len(arr[index:]), ans)

    ans = []
    leaf_nodes_helper(arr, N, ans)
    return ans