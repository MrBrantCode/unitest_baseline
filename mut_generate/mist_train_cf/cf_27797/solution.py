"""
QUESTION:
Implement the `inorder_traversal` function, which takes the root of a binary tree as input and returns the inorder traversal of the tree as a list using an iterative approach without recursion. The function should return a list of node values in the order of left subtree, current node, and right subtree. The input root node is of type `TreeNode` with attributes `value`, `left`, and `right`.
"""

from typing import List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> List[int]:
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    
    return result