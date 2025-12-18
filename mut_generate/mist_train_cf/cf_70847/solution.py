"""
QUESTION:
Reorder a binary tree while maintaining its original structure by rearranging its nodes to form a binary search tree, where for every node, all elements in the left subtree are less than the node and all elements in the right subtree are greater than the node.

Implement a function called `binaryTreeToBST(root)` that takes the root of a binary tree as input and reorders the tree in-place.
"""

class Node:

    def __init__(self, x):
        self.data = x 
        self.left = None
        self.right = None

def storeInorder(root, inorder):
    if root is None:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)

def arrayToBST(arr, root):
    if root is None:
        return
    arrayToBST(arr, root.left)
    root.data = arr[0]
    arr.pop(0)
    arrayToBST(arr, root.right)

def binaryTreeToBST(root):
    if root is None:
        return
    arr = []
    storeInorder(root, arr)
    arr.sort()
    arrayToBST(arr, root)