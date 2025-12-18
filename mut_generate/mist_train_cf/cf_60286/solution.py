"""
QUESTION:
Write a function `delete_nodes(tree, paths)` that deletes the elements at specified positions of the given binary tree and returns the new binary tree. The positions are given as a list of paths from the root of the tree to the nodes to be deleted. Each path is represented as a string of 'L' and 'R' characters, where 'L' means to go to the left child of the current node, and 'R' means to go to the right child of the current node. The binary tree is represented as a list `[root, left, right]`, where the "root", "left", and "right" are themselves binary trees. A leaf node is represented as a singleton list. The function should handle the case when a subtree is `None` and process all paths starting from the longest to avoid deleting a node that could contain nodes that also need to be deleted.
"""

def delete_nodes(tree, paths):
    if not paths or not tree:
        return tree

    paths.sort(key=len, reverse=True)
    path = paths[0]
    if len(path) == 1:
        if path == "L" and len(tree) > 1:
            tree[1] = []
        elif path == "R" and len(tree) > 2:
            tree[2] = []
    else:
        if path[0] == "L" and len(tree) > 1:
            delete_nodes(tree[1], [path[1:]])
        elif path[0] == "R" and len(tree) > 2:
            delete_nodes(tree[2], [path[1:]])

    return delete_nodes(tree, paths[1:])