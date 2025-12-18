"""
QUESTION:
Write a function `depth_first_traversal` that performs a depth-first traversal of a binary tree using an iterative method. The function should take the root node of the binary tree as input and print the values of all nodes in the tree. Assume the binary tree nodes have a `value`, `left`, and `right` attribute.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_traversal(root):
    if root is None:
        return
    
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()
        print(node.value)
        
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)