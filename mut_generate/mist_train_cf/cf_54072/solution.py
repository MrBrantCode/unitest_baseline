"""
QUESTION:
Write a function `RedNodesCount` that takes the root of a binary tree as input, where each node has a 'color' property, and returns the total number of nodes with 'red' coloration. Use Depth-First Search (DFS) traversal to visit each node exactly once.
"""

class TreeNode:
    def __init__(self, color, left=None, right=None):
        self.color = color
        self.left = left
        self.right = right

def RedNodesCount(root):
    """
    This function counts the total number of nodes with 'red' coloration in a binary tree.
    
    Parameters:
    root (TreeNode): The root of the binary tree.
    
    Returns:
    int: The total number of red nodes in the binary tree.
    """
    if root is None:
        return 0
    
    count = 1 if root.color == 'red' else 0
    
    # Recursively count the red nodes in the left and right subtrees
    count += RedNodesCount(root.left)
    count += RedNodesCount(root.right)
    
    return count