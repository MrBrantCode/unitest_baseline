"""
QUESTION:
Given the `root` of a binary search tree (BST) and an integer `val`, write a function `searchBST` that returns the path from the root to the node with value `val` as a list of node values. If no such node exists, return an empty list.

The function should take two parameters: `root` (the root of the BST) and `val` (the target value). The number of nodes in the tree is between 1 and 5000, and each node value is between 1 and 10^7.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def searchBST(root: TreeNode, val: int) -> list[int]:
    """
    Returns the path from the root to the node with value `val` as a list of node values.
    If no such node exists, returns an empty list.
    """
    def findPath(node: TreeNode, val: int, path: list[int]) -> list[int]:
        if node is None:
            return []

        path.append(node.val)

        if node.val == val:
            return path
        elif val < node.val:
            return findPath(node.left, val, path)
        else:
            return findPath(node.right, val, path)

    return findPath(root, val, [])