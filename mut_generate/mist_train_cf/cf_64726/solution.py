"""
QUESTION:
Implement a `merge_trees` function that takes two binary search tree nodes (`t1` and `t2`) as input and returns the root node of a new binary search tree that contains all elements from `t1` and `t2` while maintaining the properties of a binary search tree. Additionally, implement an `is_bst` function that takes a binary search tree node as input and returns a boolean indicating whether the tree is a valid binary search tree. The solution should be implemented without any specific test cases or example usage.
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def add_node(node, data):
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = add_node(node.left, data)
    else:
        node.right = add_node(node.right, data)

    return node

def merge_trees(t1, t2, node=None):
    if t1 is not None:
        node = add_node(node, t1.data)
        node = merge_trees(t1.left, t2, node)
        node = merge_trees(t1.right, t2, node)
    
    if t2 is not None:
        node = add_node(node, t2.data)
        node = merge_trees(t1, t2.left, node)
        node = merge_trees(t1, t2.right, node)
      
    return node

def inorder(node, values=[]):
    if node is not None:
        inorder(node.left, values)
        values.append(node.data)
        inorder(node.right, values)
    return values

def is_bst(node):
    values = inorder(node, [])
    return values == sorted(values)