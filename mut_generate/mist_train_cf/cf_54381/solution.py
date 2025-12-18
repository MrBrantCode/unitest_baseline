"""
QUESTION:
Implement a function `constructMaxBinaryTree(nums)` that takes a list of integers `nums` as input and returns the root of the maximum binary tree. The maximum binary tree is a binary tree where the parent node is the maximum of its child nodes. Also, implement a function `height(root)` that computes the height of the binary tree. 

The `constructMaxBinaryTree(nums)` function should recursively build the left and right subtrees by finding the index of the maximum number in the list and creating a root node with that value. The function should return the root of the constructed binary tree.

The `height(root)` function should compute the height of each subtree recursively and return the larger height plus one. If the root is `None`, the function should return 0.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaxBinaryTree(nums) -> 'TreeNode':
    if not nums:
        return None
    max_index = nums.index(max(nums))
    root = TreeNode(nums[max_index])
    root.left = constructMaxBinaryTree(nums[:max_index])
    root.right = constructMaxBinaryTree(nums[max_index + 1:])
    return root

def height(root) -> int:
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        if left_height < right_height:
            return right_height + 1
        else:
            return left_height + 1