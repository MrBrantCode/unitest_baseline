"""
QUESTION:
Write a function `count_nodes_with_children` that takes a binary tree node as input and returns the number of nodes in the tree that have both left and right children. The binary tree is represented as a nested dictionary where each node has a 'data' key and optional 'left' and 'right' keys representing the left and right child nodes. The function should traverse the tree recursively and count the nodes with both left and right children.
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