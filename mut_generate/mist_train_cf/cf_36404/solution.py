"""
QUESTION:
Implement a function named `construct_mapping` that takes a node representing a YAML mapping node as input. The function should return a dictionary where the keys are the duplicate keys found in the mapping node and the values are lists of line numbers where the duplicate keys occur. The node is a list of tuples, where each tuple contains a key node and a value node. The key node has a `value` attribute representing the key and a `__line__` attribute representing the line number of the key.
"""

def construct_mapping(node):
    mapping = dict()
    errors = dict()
    for key_node, value_node in node:
        key = key_node.value
        if key in mapping:
            if key in errors:
                errors[key].append(key_node.__line__)
            else:
                errors[key] = [mapping[key].__line__, key_node.__line__]
        else:
            mapping[key] = key_node
    return errors