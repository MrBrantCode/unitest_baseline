"""
QUESTION:
Design a function `max_level_sum` that calculates the maximum sum of values of nodes at any level in a binary tree, given the root of the tree. The function should return an integer representing the maximum sum. The input binary tree is represented as a TreeNode class with attributes `val` (node value), `left` (left child), and `right` (right child).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_level_sum(root):
    if root is None:
        return 0
    
    queue = [root]
    max_sum = float('-inf')

    while queue:
        level_sum = 0
        size = len(queue)
        
        for _ in range(size):
            node = queue.pop(0)
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        max_sum = max(max_sum, level_sum)
    
    return max_sum