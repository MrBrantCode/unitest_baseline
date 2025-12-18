"""
QUESTION:
Construct a binary tree from given inorder and preorder traversals such that the left subtree of each node contains only nodes with smaller values and the right subtree contains only nodes with larger values. Write a function named `buildTree` that takes two lists (inorder and preorder) and returns the root of the constructed binary tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(inorder, preorder):
    def buildTreeHelper(inorder, preorder, inStart, inEnd, preStart, preEnd):
        if inStart > inEnd:
            return None
        
        rootValue = preorder[preStart]
        root = TreeNode(rootValue)
        
        rootIndex = inorder.index(rootValue)
        
        leftCount = rootIndex - inStart
        
        root.left = buildTreeHelper(inorder, preorder, inStart, rootIndex - 1, preStart + 1, preStart + leftCount)
        
        root.right = buildTreeHelper(inorder, preorder, rootIndex + 1, inEnd, preStart + leftCount + 1, preEnd)
        
        return root
    
    return buildTreeHelper(inorder, preorder, 0, len(inorder) - 1, 0, len(preorder) - 1)