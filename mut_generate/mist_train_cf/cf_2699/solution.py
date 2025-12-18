"""
QUESTION:
Given a binary tree with nodes containing positive integer values less than or equal to 1000, implement a function `postorderTraversal` that performs an iterative post-order traversal of the tree without using recursion or built-in traversal functions, and without modifying the tree structure. The function should have a time complexity of O(n), where n is the number of nodes in the tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorderTraversal(root):
    if not root:
        return
    
    stack = []
    prev = None
    curr = root
    
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek_node = stack[-1]
            if peek_node.right and peek_node.right != prev:
                curr = peek_node.right
            else:
                result = peek_node.value
                prev = stack.pop()
                yield result