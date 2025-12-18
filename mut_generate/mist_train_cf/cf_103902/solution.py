"""
QUESTION:
Write a function `get_levels(root)` that takes the root of a binary tree as input and returns a list of lists, where each sublist contains the node data at a given level of the tree. The function should have a time complexity of O(n), where n is the number of nodes in the tree, and the order of nodes at each level does not matter. The binary tree node is defined as a class with `data`, `left`, and `right` attributes.
"""

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_levels(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    
    while queue:
        current_level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result