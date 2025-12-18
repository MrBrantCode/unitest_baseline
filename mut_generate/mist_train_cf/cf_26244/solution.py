"""
QUESTION:
Write a function `LCA` that takes as input the root of a binary tree and two nodes `p` and `q`. The function should return the least common ancestor of nodes `p` and `q` in the binary tree. The binary tree is represented as a collection of nodes where each node has a left child and a right child. The function should handle the case when either of the input nodes is the root of the tree. The function should also handle the case when the input nodes are in different subtrees of the root.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def LCA(root, p, q):
    """
    This function finds the least common ancestor of nodes p and q in a binary tree.

    Args:
    root (TreeNode): The root of the binary tree.
    p (TreeNode): The first node.
    q (TreeNode): The second node.

    Returns:
    TreeNode: The least common ancestor of nodes p and q.
    """
    # Base case
    if not root:
        return None
    
    # If either p or q matches with root's key, report the presence by returning root
    if root == p or root == q:
        return root
    
    # Look for keys in left and right subtree
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    
    # If both of the above calls return Non-NULL, then one key is present in one sub-tree and other is present in other, So this node is the LCA
    if left and right:
        return root
    
    # Otherwise check if left subtree or right subtree is LCA
    return left if left else right