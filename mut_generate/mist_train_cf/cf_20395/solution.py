"""
QUESTION:
Write a function `count_nodes_with_both_children` that counts the number of nodes in a binary tree that have both left and right children. The function should take a node of the binary tree as input, where each node is represented as a dictionary with keys "data", "left", and "right". The function should return the total count of nodes with both left and right children.
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