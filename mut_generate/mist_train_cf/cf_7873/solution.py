"""
QUESTION:
Implement a function `pre_order_traversal(node)` that takes a node of a binary tree as input, where each node can have at most two children and can hold any integer value. The function should traverse the binary tree in pre-order manner, return the sum of all nodes, and print the value of each node. Additionally, the function should also calculate the product of all nodes. The maximum number of nodes in the tree is 10^4.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def entrance(node):
    if node is None:
        return 0, 1

    left_sum, left_product = entrance(node.left)
    right_sum, right_product = entrance(node.right)
    current_sum = node.value + left_sum + right_sum
    current_product = node.value * left_product * right_product
    print(node.value)

    return current_sum, current_product