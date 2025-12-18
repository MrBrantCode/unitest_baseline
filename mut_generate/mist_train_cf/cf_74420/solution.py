"""
QUESTION:
Design an algorithm for a function `isIdentical(nodeA, nodeB)` that determines if two binary trees are identical. The function should take two binary tree nodes as input and return a boolean indicating whether the trees are identical. The function should work recursively and have a time complexity of O(n), where n is the number of nodes in the tree.
"""

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isIdentical(nodeA, nodeB):
    """
    This function determines if two binary trees are identical.

    Args:
    nodeA (TreeNode): The root of the first binary tree.
    nodeB (TreeNode): The root of the second binary tree.

    Returns:
    bool: True if the trees are identical, False otherwise.
    """
    # 1. Both trees are empty 
    if(nodeA is None and nodeB is None): 
        return True

    # 2. One of the trees is empty, but not the other
    if(nodeA is None or nodeB is None):
        return False

    # 3. Both trees are non-empty, compare them
    return(nodeA.data == nodeB.data and isIdentical(nodeA.left, nodeB.left) and isIdentical(nodeA.right, nodeB.right))