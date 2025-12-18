"""
QUESTION:
Construct the root node of a binary search tree from given preorder and inorder traversal arrays.

Given two integer arrays, `preorder` and `inorder`, which represent the preorder and inorder traversal of a binary search tree, construct the binary search tree and return its root node. The arrays are guaranteed to always allow for the construction of a valid binary search tree.

The function `buildTree` should take two parameters, `preorder` and `inorder`, both of type `List[int]`, and return a `TreeNode`. The length of `preorder` and `inorder` is between 1 and 100, and all values are unique and between 1 and 10^8.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    preorder_index = 0
    idx_map = {val:idx for idx, val in enumerate(inorder)}

    def array_to_tree(left, right):
        nonlocal preorder_index
        if left > right: return None

        root_value = preorder[preorder_index]
        root = TreeNode(root_value)

        index = idx_map[root_value]
        preorder_index += 1

        root.left = array_to_tree(left, index - 1)
        root.right = array_to_tree(index + 1, right)
        return root

    return array_to_tree(0, len(inorder) - 1)