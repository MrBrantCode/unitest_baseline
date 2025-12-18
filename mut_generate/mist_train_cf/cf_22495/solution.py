"""
QUESTION:
Create a function `create_tree_structure(dictionary)` that takes a dictionary representing a tree structure as input. Each key in the dictionary represents a node, and the value associated with each key contains information about its parent and children.

The function should return a dictionary representing the tree structure, where each key represents a node, and the value associated with each key is a dictionary containing two keys: 'parent' and 'children'. The 'parent' key should have the value of the parent node, and the 'children' key should have a list of child nodes.

Restrictions:

- The parent of the root node should be 0.
- If a node's parent does not exist in the dictionary, assign the parent of the node as None.
- If a node's children are not present in the dictionary, assign an empty list as the children of the node.
- If the dictionary is empty, return an empty dictionary as the tree structure.
"""

def create_tree_structure(dictionary):
    if not dictionary:
        return {}

    tree = {}

    # Create a dictionary to store the parents of each node
    parents = {node: {'parent': None, 'children': []} for node in dictionary.keys()}

    # Populate the parents dictionary with parent and children information
    for node, info in dictionary.items():
        parent = info['parent']
        children = info['children']

        parents[node]['children'] = children

        # Handle the case where a node's parent does not exist in the dictionary
        if parent in parents:
            parents[node]['parent'] = parent

    # Assign the parents dictionary as the value for each node in the tree structure
    for node, info in parents.items():
        tree[node] = info

    return tree