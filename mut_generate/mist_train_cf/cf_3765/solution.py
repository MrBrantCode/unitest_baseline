"""
QUESTION:
Create a function `countLeafNodes` that calculates the number of leaf nodes in a binary tree. The function should have a time complexity of O(log n), where n is the number of nodes in the binary tree, and cannot use recursion. The binary tree may be unbalanced or skewed.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def countLeafNodes(root):
    """
    Calculate the number of leaf nodes in a binary tree.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    int: The number of leaf nodes in the binary tree.
    """
    if not root:
        return 0
    
    leafCount = 0
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        if not node.left and not node.right:
            leafCount += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return leafCount