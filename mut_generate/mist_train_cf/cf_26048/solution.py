"""
QUESTION:
Create a function named `create_tree_structure` that constructs a tree structure from a given dictionary, where each key in the dictionary represents a node in the tree and its corresponding value is another dictionary containing the parent node and a list of child nodes. The function should return the root node of the constructed tree. The tree nodes should have attributes for the node value, parent node, and a list of child nodes.
"""

class TreeNode:
    def __init__(self, value=None, parent=None, children=None):
        self.value = value
        self.parent = parent
        self.children = children if children is not None else []
    
    def __repr__(self):
        return f"TreeNode({self.value}, {self.parent.value if self.parent else None}, {[c.value for c in self.children]})"
    
    def __str__(self):
        return self.__repr__()

def create_tree_structure(data):
    """
    Construct a tree structure from a given dictionary.
    
    Args:
    data (dict): A dictionary representing the tree structure, where each key is a node and its corresponding value is another dictionary containing the parent node and a list of child nodes.
    
    Returns:
    TreeNode: The root node of the constructed tree.
    """
    tree = dict()
    for k, v in data.items():
        parent = v["parent"]
        tree[k] = TreeNode(value=k, parent=tree.get(parent), children=list())
        if parent in tree:
            tree[parent].children.append(tree[k])
    # Return the root node, which is the node with parent 0
    return tree.get(0)