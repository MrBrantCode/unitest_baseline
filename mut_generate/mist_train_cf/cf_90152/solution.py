"""
QUESTION:
Implement the `min_max_leaf_nodes` function that takes the root of a binary tree as input and returns a tuple of two integers representing the minimum and maximum number of leaf nodes that can be left in the tree after deleting a node, while maintaining the height balance.

The binary tree can have at most 1000 nodes, and each node has a value and may have up to two children nodes, left and right. The height of the binary tree is at most 1000.

The function should return a tuple `(min_leaves, max_leaves)`, where `min_leaves` is the minimum number of leaf nodes that can be left in the tree after deleting a node, and `max_leaves` is the maximum number of leaf nodes that can be left in the tree after deleting a node.
"""

from typing import Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_max_leaf_nodes(root: TreeNode) -> Tuple[int, int]:
    if root is None:
        return (0, 0)
    
    left_min, left_max = min_max_leaf_nodes(root.left)
    right_min, right_max = min_max_leaf_nodes(root.right)
    
    if root.left is None and root.right is None:
        return (1, 1)
    elif root.left is None:
        return (right_min, right_max)
    elif root.right is None:
        return (left_min, left_max)
    else:
        min_leaves = min(left_min, right_min)
        max_leaves = max(left_max, right_max)
        return (min_leaves, max_leaves)