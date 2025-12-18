"""
QUESTION:
Construct a binary tree from the given inorder and preorder traversals.

Create a function called `binary_tree_from_inorder_preorder(inorder, preorder)` that takes two lists, `inorder` and `preorder`, representing the inorder and preorder traversals of a binary tree, respectively. The function should return the root node of the reconstructed binary tree. 

Restrictions: The function should use the given inorder and preorder lists only, without any additional information.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_binary_tree(inorder, preorder):
    if len(inorder) in [0, 1]:
        return Node(inorder[0]) if inorder else None

    root_val = preorder[0]
    root = Node(root_val)
    i_index = inorder.index(root_val)

    root.left = construct_binary_tree(inorder[:i_index], preorder[1:i_index + 1])
    root.right = construct_binary_tree(inorder[i_index + 1:], preorder[i_index + 1:])

    return root