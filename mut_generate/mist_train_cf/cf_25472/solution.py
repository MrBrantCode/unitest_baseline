"""
QUESTION:
Write a function `delete_node` that deletes a key from a binary search tree. The function should handle the following cases: when the key has zero children, one child, and two children. If the key has two children, the function should find the inorder successor of the key, copy its value, and then delete the key.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deleteNode(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # Find the inorder successor
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)

    return root