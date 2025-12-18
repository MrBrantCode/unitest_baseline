"""
QUESTION:
Given a sorted array. Convert it into a Height balanced Binary Search Tree (BST). Find the preorder traversal of height balanced BST. If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.
Height balanced BST means a binary tree in which the depth of the left subtree and the right subtree of every node never differ by more than 1.
Example 1:
Input: nums = {1, 2, 3, 4}
Output: {2, 1, 3, 4}
Explanation: 
The preorder traversal of the following 
BST formed is {2, 1, 3, 4}:
           2
         /   \
           1     3
               \
                4
 
Example 2:
Input: nums = {1,2,3,4,5,6,7}
Ouput: {4,2,1,3,6,5,7}
Explanation: 
The preorder traversal of the following
BST formed is {4,2,1,3,6,5,7} :
        4
       / \
      2   6
     / \  / \
    1   3 5  7
 
Your Task:
You don't need to read or print anything. Your task is to complete the function sortedArrayToBST() which takes the sorted array nums as input paramater and returns the preorder traversal of height balanced BST. If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
Constraints:
1 ≤ |nums| ≤ 10^{4}
-10^{4} ≤ nums[i] ≤ 10^{4}
"""

class TreeNode:
    def __init__(self, d):
        self.val = d
        self.left = None
        self.right = None

def preOrder(root, ans):
    if not root:
        return
    ans.append(root.val)
    preOrder(root.left, ans)
    preOrder(root.right, ans)

def insert(root, val):
    if not root:
        root = TreeNode(val)
        return root
    if root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def build_bst(root, nums, l, r):
    if l > r:
        return root
    mid = (l + r) // 2
    root = insert(root, nums[mid])
    root.left = build_bst(root.left, nums, l, mid - 1)
    root.right = build_bst(root.right, nums, mid + 1, r)
    return root

def sorted_array_to_bst_preorder(nums):
    ans = []
    if len(nums) == 0:
        return ans
    root = build_bst(None, nums, 0, len(nums) - 1)
    preOrder(root, ans)
    return ans