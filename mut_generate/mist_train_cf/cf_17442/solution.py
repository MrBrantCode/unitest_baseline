"""
QUESTION:
Convert the given binary tree to a doubly linked list in-place without using any extra data structures. The conversion should be done in a depth-first manner, with the left pointer of each node pointing to the previous node and the right pointer pointing to the next node in the doubly linked list. The resulting doubly linked list should be sorted in ascending order based on node values. Implement this conversion using the `convertToDoublyLinkedList(root)` function.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def convertToDoublyLinkedList(root):
    prev = None
    def inorder(node):
        nonlocal prev
        if not node:
            return
        inorder(node.left)
        nonlocal prev
        node.left = prev
        if prev:
            prev.right = node
        prev = node
        inorder(node.right)
    inorder(root)
    while prev and prev.left:
        prev = prev.left
    return prev