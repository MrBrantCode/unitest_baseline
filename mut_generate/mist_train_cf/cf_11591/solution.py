"""
QUESTION:
Write a function `buildTree` that constructs a binary tree from the given inorder and preorder traversals. The binary tree should be constructed in such a way that the left subtree of each node contains only nodes with smaller values, and the right subtree contains only nodes with larger values. The function should take two lists as input: `inorder` and `preorder`, representing the inorder and preorder traversals respectively. The function should return the root node of the constructed binary tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(inorder, preorder):
    def helper(inStart, inEnd, preStart, preEnd):
        if inStart > inEnd:
            return None
        
        rootValue = preorder[preStart]
        root = TreeNode(rootValue)
        
        rootIndex = inorder.index(rootValue)
        
        leftCount = rootIndex - inStart
        
        root.left = helper(inStart, rootIndex - 1, preStart + 1, preStart + leftCount)
        
        root.right = helper(rootIndex + 1, inEnd, preStart + leftCount + 1, preEnd)
        
        return root
    
    return helper(0, len(inorder) - 1, 0, len(preorder) - 1)