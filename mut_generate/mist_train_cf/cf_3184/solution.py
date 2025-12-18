"""
QUESTION:
Write a recursive function named `depth_first_search` that performs a depth-first search on a tree with a variable number of children for each node. The function should take the tree as input and return a dictionary where the keys are the nodes visited during the search and the values are their respective depths in the tree. The tree is defined as an object with a `root` attribute, and each node has a `children` attribute that is a list of child nodes.
"""

def depth_first_search(tree):
    visited = {}  

    def dfs(node, depth):
        if node is None:
            return
        visited[node] = depth
        for child in node.children:
            dfs(child, depth + 1)

    dfs(tree.root, 0)
    return visited