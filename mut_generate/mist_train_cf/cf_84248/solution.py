"""
QUESTION:
Write a function `search_tree` that takes a binary tree and a target value as input and returns a boolean indicating whether the value exists in the tree. The binary tree is represented as a nested dictionary where each node has a "value" and optional "left" and "right" child nodes. The function should use recursion to search the tree.
"""

def search_tree(tree, value):
    """
    This function recursively searches a binary tree for a given value.
    
    Parameters:
    tree (dict): A dictionary representing a binary tree where each node has a "value" and optional "left" and "right" child nodes.
    value (any): The target value to search for in the tree.
    
    Returns:
    bool: True if the value exists in the tree, False otherwise.
    """
    # Check if tree is not empty
    if tree is not None:
        # Check if current node's value is the value we are looking for
        if tree["value"] == value:
            return True
        # Search in left subtree
        if "left" in tree and search_tree(tree["left"], value):
            return True
        # Search in right subtree
        if "right" in tree and search_tree(tree["right"], value):
            return True
    # Return False if the value was not found in the tree
    return False