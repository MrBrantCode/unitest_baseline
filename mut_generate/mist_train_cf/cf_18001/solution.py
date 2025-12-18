"""
QUESTION:
Write a recursive function called `dfs` that performs a depth-first search on a binary tree and returns a dictionary mapping each node's value to its depth in the tree. The function should take in a node as input and have a default `depth` parameter set to 0. Assume that the binary tree is represented by a Node class with `value`, `left`, and `right` attributes.
"""

def dfs(node, depth=0):
    visited = {}
    if node is not None:
        visited[node.value] = depth
        visited.update(dfs(node.left, depth+1))
        visited.update(dfs(node.right, depth+1))
    return visited