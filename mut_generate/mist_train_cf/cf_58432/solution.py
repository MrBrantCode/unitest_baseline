"""
QUESTION:
Create a function named `build_tree` that constructs a hierarchical tree architecture from a given dictionary representing parent-child relationships amongst nodes. The dictionary should be in the format `{node_id: {'parent': parent_id, 'children': [child_id1, child_id2, ...]}}`. The function should return a dictionary where each key is a node id and its corresponding value is a Node object with attributes `id`, `parent`, and `children`. The `parent` attribute should be a Node object representing the parent node, and the `children` attribute should be a list of Node objects representing the child nodes.
"""

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = []

def build_tree(tree_dict):
    # create node objects for each unique id in dictionary
    nodes = {id: Node(id) for id in tree_dict.keys()}

    # set parent - children relationships
    for id, node in nodes.items():
        if tree_dict[id]['parent'] != 0:  # if the node has a parent
            parent_id = tree_dict[id]['parent']
            node.parent = nodes[parent_id]  # set parent
            nodes[parent_id].children.append(node)  # add current node to parent's children list

    return nodes