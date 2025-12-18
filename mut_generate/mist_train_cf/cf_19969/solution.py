"""
QUESTION:
Write a function called `max_nodes_in_height_balanced_tree` that takes an integer `h` as input, representing the height of a height-balanced binary tree where each node has at least 2 children, and returns the maximum number of nodes in the tree. The function should not take any additional inputs and should not print any output.
"""

def max_nodes_in_height_balanced_tree(h):
    max_nodes = 0

    for level in range(h, -1, -1):
        nodes_at_level = 2**(level) - 1
        max_nodes += nodes_at_level

    return max_nodes