"""
QUESTION:
Given a binary tree with a root node, write a function `find_depths(root)` that returns the minimum and maximum depths of the tree. The minimum depth is the minimum number of nodes along the shortest path from the root node to any leaf node, while the maximum depth is the maximum number of nodes along the longest path from the root node to any leaf node.

Also, write another function `is_balanced(root)` that checks if the binary tree is balanced. A binary tree is considered balanced if the difference between the minimum and maximum depths is at most 1.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_depths(root):
    if not root:
        return 0, 0
    
    left_min, left_max = find_depths(root.left)
    right_min, right_max = find_depths(root.right)
    
    min_depth = min(left_min, right_min) + 1 if left_min or right_min else 1
    max_depth = max(left_max, right_max) + 1
    
    return min_depth, max_depth

def is_balanced(root):
    min_depth, max_depth = find_depths(root)
    return max_depth - min_depth <= 1