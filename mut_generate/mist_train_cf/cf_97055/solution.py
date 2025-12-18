"""
QUESTION:
Given a binary tree with nodes containing integer values (which can be negative), implement a function `pre_order(node)` that traverses the tree in pre-order manner and returns the sum and product of all nodes. The function should handle cases where the input node is None.
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def pre_order(node):
    if node is None:
        return 0, 1
    
    sum_left, product_left = pre_order(node.left)
    sum_right, product_right = pre_order(node.right)
    
    current_sum = node.data + sum_left + sum_right
    current_product = node.data * product_left * product_right
    
    return current_sum, current_product