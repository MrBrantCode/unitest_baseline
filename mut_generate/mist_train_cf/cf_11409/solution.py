"""
QUESTION:
Find the first common ancestor of two nodes in a binary search tree. 

The function should take as input the root of the binary search tree and the values of two target nodes. The function should return the node with the value of the first common ancestor. 

The function should have a time complexity of O(log n) in the average case, where n is the number of nodes in the tree.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def first_common_ancestor(root, p, q):
    """
    Finds the first common ancestor of two nodes in a binary search tree.
    
    Args:
    root: The root of the binary search tree.
    p: The value of the first target node.
    q: The value of the second target node.
    
    Returns:
    The node with the value of the first common ancestor.
    """
    if not root:
        return None

    if p < root.value and q < root.value:
        return first_common_ancestor(root.left, p, q)
    elif p > root.value and q > root.value:
        return first_common_ancestor(root.right, p, q)
    else:
        return root