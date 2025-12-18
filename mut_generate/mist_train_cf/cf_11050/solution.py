"""
QUESTION:
Implement a function `dfs_binary_tree` that performs a depth-first search on a binary tree. The function should take the root node of the binary tree as input and return a list of all node values visited during the search, in the order they were visited. Assume the binary tree nodes have a `value`, `left`, and `right` attribute.
"""

def dfs_binary_tree(node):
    """
    Performs a depth-first search on a binary tree and returns a list of node values visited.

    Args:
    node: The root node of the binary tree.

    Returns:
    A list of node values visited during the search.
    """
    if node is None:
        return []
    return [node.value] + dfs_binary_tree(node.left) + dfs_binary_tree(node.right)