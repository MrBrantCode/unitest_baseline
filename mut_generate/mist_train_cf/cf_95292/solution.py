"""
QUESTION:
Construct a function named buildTree that takes two parameters: inorder and preorder, both lists of integers representing the inorder and preorder traversals of a binary tree. The function should return the root of the constructed binary tree. The binary tree should be constructed such that for each node, its left subtree contains only nodes with smaller values, and its right subtree contains only nodes with larger values.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def buildTree(inorder, preorder):
    if len(inorder) == 0 and len(preorder) == 0:
        return None
    root = preorder[0]
    rootIndex = inorder.index(root)
    node = TreeNode(root)
    node.left = buildTree(inorder[:rootIndex], preorder[1:1+rootIndex])
    node.right = buildTree(inorder[rootIndex+1:], preorder[rootIndex+1:])
    return node