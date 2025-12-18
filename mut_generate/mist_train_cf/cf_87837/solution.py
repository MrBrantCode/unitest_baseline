"""
QUESTION:
Write a recursive function `depth_first_search` that performs a depth-first search on a tree with a variable number of children per node. The function should take the tree as input and return a dictionary where the keys are the visited nodes and the values are their respective depths in the tree. The tree is represented as a node with a list of children.
"""

def depth_first_search(tree):
    visited = {}  # Dictionary to store visited nodes and their depths

    def dfs(node, depth):
        if node is None:
            return
        visited[node] = depth
        for child in node.children:
            dfs(child, depth + 1)

    dfs(tree.root, 0)
    return visited