"""
QUESTION:
Implement a function named `balanceAndCalculateDiameter` that takes the root of a binary tree as input, balances the tree, and then returns the diameter of the balanced tree. The tree is balanced if for every node in the tree, the difference in height between its left subtree and its right subtree is no more than 1. The diameter of a binary tree is the maximum length of the path between any two nodes in a tree. This path may or may not pass through the root.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def balanceTree(arr):
    if not arr:
        return None
 
    mid = len(arr) // 2
 
    root = Node(arr[mid])
    root.left = balanceTree(arr[:mid])
    root.right = balanceTree(arr[mid+1:])
    return root

def storeInorder(root, inorder):
    if not root:
        return
    
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)

def diameter(root):
    if root is None:
        return 0
 
    lheight = height(root.left)
    rheight = height(root.right)
 
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
 
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

def balanceAndCalculateDiameter(root):
    arr = []
    storeInorder(root, arr)
    arr.sort()
    root = balanceTree(arr)
    return diameter(root)