"""
QUESTION:
Implement the `travelLeafNode` function, which calculates the sum of all leaf nodes in a given JSON tree. The JSON tree is represented as a nested dictionary where keys are strings and values can be dictionaries, lists, or integers. A leaf node is a node that does not have any children (i.e., it is an integer). The function should recursively traverse the tree and return the total sum of all leaf nodes.
"""

import json

def travelLeafNode(json_tree):
    leaf_sum = 0
    if isinstance(json_tree, dict):
        for value in json_tree.values():
            leaf_sum += travelLeafNode(value)
    elif isinstance(json_tree, list):
        for item in json_tree:
            leaf_sum += travelLeafNode(item)
    else:
        leaf_sum += json_tree
    return leaf_sum