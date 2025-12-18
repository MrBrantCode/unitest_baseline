"""
QUESTION:
Construct a binary tree from the given preorder and inorder traversal sequences. Implement the `build_tree` function with the following restrictions: 
- The function should take two parameters: `preorder` and `inorder`, which are lists of integers representing the preorder and inorder traversal sequences, respectively.
- The function should return the root node of the constructed binary tree.
- The binary tree node is defined by the `TreeNode` class with attributes `val`, `left`, and `right`.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def entrance(preorder, inorder):
    if not preorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    root_index = inorder.index(root_val)

    root.left = entrance(preorder[1:1 + root_index], inorder[:root_index])
    root.right = entrance(preorder[1 + root_index:], inorder[root_index + 1:])

    return root