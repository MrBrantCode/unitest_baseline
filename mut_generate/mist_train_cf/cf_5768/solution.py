"""
QUESTION:
Write a function `count_nodes_with_children` that takes the root node of a binary tree as input and returns the number of nodes in the tree that have both left and right children. Each node in the tree is represented as a dictionary with keys 'data', 'left', and 'right', where 'data' is the node's value, 'left' is the left child node, and 'right' is the right child node. Assume that the input tree is non-empty and all nodes have the same structure.
"""

def count_nodes_with_children(node):
    if node is None:
        return 0
    
    count = 0
    if node.get('left') and node.get('right'):
        count = 1
    
    count += count_nodes_with_children(node.get('left'))
    count += count_nodes_with_children(node.get('right'))
    
    return count