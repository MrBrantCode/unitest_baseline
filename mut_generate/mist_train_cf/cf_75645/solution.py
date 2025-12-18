"""
QUESTION:
Create a function `build_tree` that takes a dictionary representing the parent-child relationships between nodes and returns the root node of the constructed tree. The dictionary keys are the node IDs, and each value is another dictionary containing the parent ID and a list of child IDs.

Restrictions:

- The input dictionary is a valid representation of a tree, where each node has a unique ID and a single parent (except for the root node, which has a parent ID of 0).
- The function should return the root node of the constructed tree.
"""

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

def build_tree(tree_dict):
    tree = {}
    for id, info in tree_dict.items():
        node = Node(id)
        tree[id] = node
        parent_id = info['parent']
        if parent_id in tree:
            tree[parent_id].children.append(node)

    # find the root node
    for id, node in tree.items():
        if id == 1 or (id != 1 and tree[id].id not in [child.id for node in tree.values() for child in node.children]):
            return tree[id]