"""
QUESTION:
Implement the `link_shared_paths(root)` function which takes the root node of a file system tree as input and modifies the tree in place by linking shared directories. A shared directory is one that appears in multiple paths in the file system, and when encountered, it should be linked to the existing instance of the directory to avoid duplication.
"""

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def link_shared_paths(root):
    shared_directories = {}

    def dfs(node, path):
        if node.name in shared_directories:
            path.append(shared_directories[node.name])
            return

        new_node = TreeNode(node.name)
        shared_directories[node.name] = new_node
        path.append(new_node)

        for child in node.children:
            dfs(child, new_node.children)

    dfs(root, [])
    return root