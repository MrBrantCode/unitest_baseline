"""
QUESTION:
Implement a tree data structure with the following properties: each node is a structured data type containing its label, a list of references to its child nodes, and a reference to its parent node. The tree should have 20 nodes with the specified hierarchy: A is the root node with child nodes B, C, and D. B has child nodes E, F, and P. C has nodes G, H, and Q. D has nodes I, J, and R. F has nodes K, L, and S. Q has nodes M, N, and T. R has nodes O, U, and V. 

The implementation should include two functions: `find_node(root, label)` to locate any node by its label using depth-first search and `compute_depth(node)` to calculate the height or depth of any specified node.
"""

class Node:
    def __init__(self, label, parent=None):
        self.label = label
        self.children = []
        self.parent = parent

def entrance(root, label):
    if root.label == label:
        return root
    for child in root.children:
        result = entrance(child, label)
        if result:
            return result
    return None

def compute_depth(node):
    depth = 0
    while node.parent is not None:
        depth += 1
        node = node.parent
    return depth