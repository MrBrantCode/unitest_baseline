"""
QUESTION:
Write a function `find_common_ancestor` that takes the root of a binary tree and two nodes as input and returns the first common ancestor of the two nodes in the binary tree. The binary tree node is represented as an object with a value and two children (left and right). Assume the nodes exist in the tree and are not the same node.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_common_ancestor(root, node1, node2):
    """
    This function finds the first common ancestor of two nodes in a binary tree.

    Args:
    root (TreeNode): The root of the binary tree.
    node1 (TreeNode): The first node.
    node2 (TreeNode): The second node.

    Returns:
    TreeNode: The first common ancestor of node1 and node2.
    """
    if root is None:
        return None
    
    if root == node1 or root == node2:
        return root

    left_ancestor = find_common_ancestor(root.left, node1, node2)
    right_ancestor = find_common_ancestor(root.right, node1, node2)

    if left_ancestor and right_ancestor:
        return root

    return left_ancestor if left_ancestor is not None else right_ancestor