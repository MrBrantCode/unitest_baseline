"""
QUESTION:
Construct a function named `is_balanced` to detect if a binary tree is balanced. The function takes the root of a binary tree as input and returns `True` if the binary tree is balanced, `False` otherwise. The binary tree is balanced if the heights of the two subtrees of any node never differ by more than 1.
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