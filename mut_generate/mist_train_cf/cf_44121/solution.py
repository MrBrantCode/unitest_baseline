"""
QUESTION:
Construct a binary tree from the given preorder and inorder traversals and calculate the height of the constructed tree.

Given two integer arrays `preorder` and `inorder`, where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, implement a function `buildTreeAndReturnHeight(preorder, inorder)` that constructs and returns the binary tree along with its height.

Restrictions: `1 <= preorder.length <= 5000`, `inorder.length == preorder.length`, `-5000 <= preorder[i], inorder[i] <= 5000`, `preorder` and `inorder` consist of unique values, and each value of `inorder` also appears in `preorder`.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTreeHelper(preorder, preStart, inStart, inEnd, inorderDict):
    if preStart > len(preorder) - 1 or inStart > inEnd: 
        return None
    root = TreeNode(preorder[preStart])
    inIndex = inorderDict[root.val]
    root.left = buildTreeHelper(preorder, preStart + 1, inStart, inIndex - 1, inorderDict)
    root.right = buildTreeHelper(preorder, preStart + inIndex - inStart + 1, inIndex + 1, inEnd, inorderDict) 
    return root

def buildTreeAndReturnHeight(preorder, inorder):
    inorderDict = {num: index for index, num in enumerate(inorder)}  # value to index mapping
    root = buildTreeHelper(preorder, 0, 0, len(inorder) - 1, inorderDict)

    def height(root):
        if root is None:
            return 0
        return max(height(root.left), height(root.right)) + 1

    return root, height(root)