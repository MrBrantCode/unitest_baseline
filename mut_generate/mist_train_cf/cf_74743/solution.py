"""
QUESTION:
Write a function `count_twigs(node)` that counts the number of twig nodes in a binary tree. A twig node is a node with no children, i.e., it has no 'left' or 'right' values. The input `node` is a dictionary representing the binary tree, where each node is a dictionary with a 'data' key and optional 'left' and 'right' keys. The function should recursively traverse the tree and return the total count of twig nodes.
"""

def count_twigs(node):
    if node is None:
        return 0
    elif 'left' not in node and 'right' not in node:
        return 1
    else:
        left_twig_count = count_twigs(node.get('left')) if 'left' in node else 0
        right_twig_count = count_twigs(node.get('right')) if 'right' in node else 0
        return left_twig_count + right_twig_count