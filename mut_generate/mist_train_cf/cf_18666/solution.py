"""
QUESTION:
Construct a function called `buildTree` that takes two lists, `inorder` and `preorder`, representing the inorder and preorder traversals of a binary tree. The function should return the root of the constructed binary tree where for each node, all elements in the left subtree are smaller than the node's value, and all elements in the right subtree are larger than the node's value. Assume that the input lists are valid and do not contain duplicate values.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def buildTree(inorder, preorder):
    """
    Construct a binary tree from the given inorder and preorder traversals.
    
    Parameters:
    inorder (list): Inorder traversal of the binary tree.
    preorder (list): Preorder traversal of the binary tree.
    
    Returns:
    TreeNode: The root of the constructed binary tree.
    """
    if len(inorder) == 0 and len(preorder) == 0:
        return None
    root = preorder[0]
    rootIndex = inorder.index(root)
    node = TreeNode(root)
    node.left = buildTree(inorder[:rootIndex], preorder[1:rootIndex+1])
    node.right = buildTree(inorder[rootIndex+1:], preorder[rootIndex+1:])
    return node