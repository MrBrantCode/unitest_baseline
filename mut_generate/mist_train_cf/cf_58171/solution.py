"""
QUESTION:
Create a function `binary_tree` and `in_order` (or any other traversal method) to construct a binary tree from a given string array and find the deepest node. The binary tree is constructed by setting the first element as the root, the second element as the left child, and the third element as the right child, and so on. The function should take a string array as input and return the deepest node in the binary tree. Assume the input array is ["李", "張", "王", "趙", "劉"] and the deepest node is defined by in-order traversal.
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def construct_binary_tree(nodes):
    def binary_tree(nodes, root, i, n):
        if i < n:
            temp = Node(nodes[i])
            root = temp

            # construct left child
            root.left = binary_tree(nodes, root.left, 2 * i + 1, n)

            # construct right child
            root.right = binary_tree(nodes, root.right, 2 * i + 2, n)
        return root

    def in_order(node):
        if node is not None:
            in_order(node.left)
            nonlocal deepest_node 
            deepest_node = node.data
            in_order(node.right)

    root = None
    last_index = len(nodes)
    deepest_node = None
    root = binary_tree(nodes, root, 0, last_index)
    in_order(root)
    return deepest_node