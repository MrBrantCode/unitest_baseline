"""
QUESTION:
Construct a function `is_balanced` that determines if a binary tree is balanced. The function takes the root of a binary tree as input and returns a boolean value indicating whether the binary tree is balanced. A binary tree is balanced if the heights of the two subtrees of any node never differ by more than 1. The height of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def helper(node):
        if node is None:
            return True, 0
        
        left_balanced, left_height = helper(node.left)
        right_balanced, right_height = helper(node.right)
        
        if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
            return False, 0
        
        return True, max(left_height, right_height) + 1
    
    return helper(root)[0]