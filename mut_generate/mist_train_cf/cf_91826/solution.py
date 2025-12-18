"""
QUESTION:
Write a function called `sum_and_max` that takes the root of a binary tree with nodes containing positive integers as input. The function should return a tuple containing the sum of all nodes in the tree and the maximum value present in the tree. Assume the tree nodes have attributes `value`, `left`, and `right` representing the node's value and its left and right child nodes respectively.
"""

def sum_and_max(node):
    if node is None:
        return 0, 0
    
    left_sum, left_max = sum_and_max(node.left)
    right_sum, right_max = sum_and_max(node.right)
    
    current_sum = node.value + left_sum + right_sum
    current_max = max(node.value, left_max, right_max)
    
    return current_sum, current_max