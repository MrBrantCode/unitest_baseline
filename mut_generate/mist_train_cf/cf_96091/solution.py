"""
QUESTION:
Implement a function named `count_nodes_with_both_children` that takes a binary tree node as input and returns the count of nodes in the binary tree that have both left and right children. Each node is a dictionary containing the keys "data", "left", and "right", where "data" is the node's value and "left" and "right" are the left and right child nodes, respectively. The function should handle trees of any depth.
"""

def count_nodes_with_both_children(node):
    if node is None:
        return 0

    count = 0

    if node.get("left") and node.get("right"):
        count += 1

    count += count_nodes_with_both_children(node.get("left"))
    count += count_nodes_with_both_children(node.get("right"))

    return count