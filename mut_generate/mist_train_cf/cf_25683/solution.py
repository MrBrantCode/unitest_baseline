"""
QUESTION:
Given two binary trees, merge them into a new binary tree where the values of each node in the new tree are the sum of the corresponding nodes in the input trees. If a node in one tree has no corresponding node in the other tree, the node from the single tree is carried over to the merged tree. The function name is `mergeTrees(t1, t2)`.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(t1, t2):
    """
    Merge two binary trees into a new binary tree where the values of each node 
    in the new tree are the sum of the corresponding nodes in the input trees.

    Args:
    t1 (TreeNode): The first binary tree.
    t2 (TreeNode): The second binary tree.

    Returns:
    TreeNode: The merged binary tree.
    """
    # Exit case, if one of the trees is null
    if not t1 or not t2:
        return t1 or t2

    # Otherwise, merge the new node values from both trees
    t3 = TreeNode(t1.val + t2.val)

    # Recursively traverse both trees to build up the result
    t3.left = mergeTrees(t1.left, t2.left)
    t3.right = mergeTrees(t1.right, t2.right)

    return t3