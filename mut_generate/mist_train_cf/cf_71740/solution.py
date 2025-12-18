"""
QUESTION:
Convert a binary tree to a doubly linked list using in-order traversal. The function should take the root of the binary tree as input and return the head of the doubly linked list. The function should not use any extra space that scales with input size (i.e., it should use constant space). The function should have a time complexity of O(n), where n is the number of nodes in the binary tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def btreeToDLL(root):
    head = None
    prev_node = None

    def inorder(node):
        nonlocal head, prev_node
        if node is None:
            return
        inorder(node.left)
        temp = DNode(node.data)
        if prev_node is None:
            head = temp
        else:
            temp.prev = prev_node
            prev_node.next = temp
        prev_node = temp
        inorder(node.right)

    inorder(root)
    return head