"""
QUESTION:
Given an array of N-ary tree nodes with unique values, where each node has a value and a list of its children, create two functions: `findRoot` and `findRootWithConstantSpace`. The `findRoot` function should find the root of the N-ary tree in linear time complexity and any space complexity, while the `findRootWithConstantSpace` function should find the root in linear time complexity and constant space complexity. The total number of nodes in the array varies between 1 and 5 * 10^4.
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def findRoot(nodes):
    child_nodes_set = {child for node in nodes for child in node.children}
    for node in nodes:
        if node not in child_nodes_set:
            return node
    return None

def findRootWithConstantSpace(nodes):
    total_sum = sum(node.val for node in nodes)
    child_node_sum = sum(child.val for node in nodes for child in node.children)
    for node in nodes:
        if total_sum - node.val == child_node_sum:
            return node
    return None