"""
QUESTION:
Implement a solution for cloning an N-ary tree and searching for a node by its value. The solution should include two methods: `cloneTree(Node root)` and `findNode(int val)`.

The `cloneTree(Node root)` method should return a deep copy of the input N-ary tree. Each node in the N-ary tree contains a unique value, a list of its children, and a parent pointer.

The `findNode(int val)` method should return the node with the given value in the cloned tree. If the value does not exist, it should return `None`.

The N-ary tree is defined by a class `Node` with attributes `val`, `parent`, and `children`. The depth of the tree is less than or equal to 1000, and the total number of nodes is between 0 and 10^4. The value of each node is unique.
"""

class Node:
    def __init__(self, val, parent = None, children = None):
        self.val = val
        self.parent = parent
        self.children = children if children else []

def entrance(root, val):
    """
    Clone an N-ary tree and search for a node by its value.

    Args:
        root (Node): The root of the N-ary tree.
        val (int): The value to search for in the cloned tree.

    Returns:
        Node: The cloned tree and the node with the given value if found, otherwise None.
    """

    clones = {}

    def cloneTree(node):
        if not node:
            return None

        clone = Node(node.val)
        clones[clone.val] = clone
        clone.children = [cloneTree(child) for child in node.children]
        
        for child in clone.children:
            child.parent = clone
        
        return clone

    cloned_root = cloneTree(root)
    node = clones.get(val, None)
    return cloned_root, node