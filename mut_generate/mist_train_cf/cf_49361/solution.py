"""
QUESTION:
Develop a recursive function `find_shortest_path` that traverses a balanced tree using a depth-first search strategy and returns the shortest path from the root node to a specified node. The function should take a tree and a goal node ID as input and return a list of node IDs representing the shortest path. If no path exists, the function should return None.

Implement a custom dynamic backtracking mechanism and use a heuristic approach to determine the shortest distances. The tree structure consists of nodes with unique IDs and data, and each node may have multiple children. Assume the tree does not contain loops or self-pointing nodes.

Note: The input tree will be a balanced tree data structure, where each node is represented as an object with an ID, data, and a list of children. The root node of the tree will be provided, and the goal node ID will be a unique identifier for the target node.
"""

class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.children = []
        self.parent = None

class Tree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, id, data, parent_id=None):
        node = Node(id, data)

        if self.root is None:
            self.root = node
        else:
            parent = self.nodes[parent_id]
            parent.children.append(node)
            node.parent = parent

        self.nodes[id] = node

def dfs(tree, node, goal, path):
    path.append(node.id)

    if node.id == goal:
        return path

    for child in node.children:
        result = dfs(tree, child, goal, list(path))

        if result is not None:
            return result

    return None

def find_shortest_path(tree, goal):
    return dfs(tree, tree.root, goal, [])