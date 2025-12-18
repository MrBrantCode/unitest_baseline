"""
QUESTION:
Write a function named `find_proximate_common_progenitor` that identifies the most proximate shared progenitor found within a binary search tree configuration for two given nodes. The function should take as input the root node of the binary search tree and the values of the two nodes for which to find the common progenitor. Ensure the function is thread-safe and optimized for large datasets.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_proximate_common_progenitor(root, p, q):
    """
    This function finds the most proximate shared progenitor for two nodes in a binary search tree.

    Args:
        root (TreeNode): The root node of the binary search tree.
        p (int): The value of the first node.
        q (int): The value of the second node.

    Returns:
        TreeNode: The most proximate common progenitor for the two nodes.

    """
    # If the tree is empty, return None
    if not root:
        return None

    # If both p and q are less than the root's value, move to the left subtree
    if p < root.val and q < root.val:
        return find_proximate_common_progenitor(root.left, p, q)

    # If both p and q are greater than the root's value, move to the right subtree
    if p > root.val and q > root.val:
        return find_proximate_common_progenitor(root.right, p, q)

    # If neither of the above conditions is true, the root is the most proximate common progenitor
    return root