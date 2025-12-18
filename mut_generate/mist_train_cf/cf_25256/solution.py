"""
QUESTION:
Construct a binary tree from a given pre-order traversal sequence. The function should be named `construct_tree` and should take a list of node values as input. The constructed tree should have a binary tree structure where each node has a value, a left child, and a right child.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(preorder):
    if not preorder:
        return None

    val = preorder[0]
    preorder.pop(0)
    node = Node(val)

    smaller = []
    greater = []
    temp = []

    while preorder and preorder[0] < val:
        smaller.append(preorder.pop(0))
    
    while preorder and preorder[0] > val:
        temp.append(preorder.pop(0))
    
    greater = temp

    node.left = construct_tree(smaller)
    node.right = construct_tree(greater)

    return node