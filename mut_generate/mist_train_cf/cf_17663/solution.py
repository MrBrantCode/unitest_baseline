"""
QUESTION:
Write a function named `iterative_inorder_traversal` that performs an in-order traversal of a binary search tree using an iterative approach. The function should handle binary search trees that may be unbalanced and contain duplicate values. The function should not use a recursive approach.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def iterative_inorder_traversal(root):
    """
    Performs an in-order traversal of a binary search tree using an iterative approach.
    
    Args:
    root (TreeNode): The root of the binary search tree.
    
    Returns:
    list: A list of node values in the order they were visited.
    """
    result = []
    stack = []
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            node = stack.pop()
            result.append(node.val)
            current = node.right

    return result