"""
QUESTION:
Implement a function named `verify_bst_validity` that takes in two lists: `nodes_list` and `values_list`. `nodes_list` contains the node relationships in a binary search tree (BST) where 'root' indicates the root node, 'left' indicates the left child of the current node, and 'right' indicates the right child of the current node. `values_list` contains the values to be inserted into the BST corresponding to the relationships in `nodes_list`. 

The function should return True if the constructed BST is valid, and False otherwise. A valid BST is a binary tree where for any given node, all elements in the left subtree are less than the node and all elements in the right subtree are greater than the node. The function should use a helper function `is_bst` to check the validity of the BST. 

The `is_bst` function takes in a node, a minimum value, and a maximum value, and returns True if the subtree rooted at the node is a valid BST, and False otherwise. The function should also use another helper function `insert` to construct the BST. The `insert` function takes in the root of the BST and a value, and returns the root of the updated BST after inserting the value. 

The function should handle the case where the input lists are empty or contain only one element.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.val < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root

def is_bst(node, min_val, max_val):
    if node is None:
        return True
    if node.val < min_val or node.val > max_val:
        return False
    return is_bst(node.left, min_val, node.val -1) and is_bst(node.right, node.val+1, max_val)

def verify_bst_validity(nodes_list, values_list):
    root = None
    for relation, value in zip(nodes_list, values_list):
        if relation == 'root':
            root = Node(value)
        else:
            root = insert(root,value)
    is_valid = is_bst(root, float('-inf'), float('inf'))
    return is_valid