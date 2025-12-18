"""
QUESTION:
Implement a function `find_values_greater_than_x(root, x)` that uses a depth-first search strategy with both pre-order and post-order traversal methods to find all nodes in a ternary tree that have a value greater than `x`, where `x` is an integer value and `root` is the root node of the ternary tree. The function should return a list of node values that meet the condition.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.mid = self.right = None

def find_values_greater_than_x(root, x):
    output = set()

    def pre_order_traversal(node):
        if node is None:
            return
        if node.value > x:
            output.add(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.mid)
        pre_order_traversal(node.right)

    def post_order_traversal(node):
        if node is None:
            return
        post_order_traversal(node.left)
        post_order_traversal(node.mid)
        post_order_traversal(node.right)
        if node.value > x:
            output.add(node.value)

    pre_order_traversal(root)
    post_order_traversal(root)
    return list(output)