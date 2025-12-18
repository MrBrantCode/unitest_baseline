"""
QUESTION:
Write a code that includes two functions: `zigzag_traversal(root)` and `calculate_sum(root)`. 

Function `zigzag_traversal(root)` should perform an iterative zigzag traversal on a binary tree and return a list of node values in the order they were visited. The root of the binary tree is passed as the function argument.

Function `calculate_sum(root)` should calculate the sum of all the nodes in the binary tree. The root of the binary tree is passed as the function argument.

Assume that the binary tree nodes have a `val` attribute for the node's value, and `left` and `right` attributes for the left and right children, respectively. If a node does not exist, it is represented by `None`.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigzag(root):
    if root is None:
        return []

    result = []
    current_level = [root]
    level = 1

    while current_level:
        current_values = []
        next_level = []

        for node in current_level:
            current_values.append(node.val)
            
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if level % 2 == 0:
            result.extend(current_values[::-1])
        else:
            result.extend(current_values)
        
        current_level = next_level
        level += 1

    return result

def calculateSum(root):
    if root is None:
        return 0

    stack = [root]
    total_sum = 0

    while stack:
        node = stack.pop()
        total_sum += node.val

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return total_sum