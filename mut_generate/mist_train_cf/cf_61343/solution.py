"""
QUESTION:
Write a function named `construct_tree` that constructs a tree chart visualization using the provided dataset with different levels based on the categories. The function should take a list of tuples `data` as input, where each tuple contains a name and a category. The function should return the root of the constructed tree. 

Additionally, write a function named `print_pre_order` that prints the tree chart in a pre-order traversal manner. The function should take the root of the tree as input and print the value of each node in pre-order traversal.

Restrictions: 
- The tree chart should accommodate multiple children for each node.
- The tree chart should be constructed based on the categories in the dataset.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)

def construct_tree(data):
    root = TreeNode("Dataset")
    categories = {}
    for name, category in data:
        if category in categories:
            node = TreeNode(name)
            categories[category].append(node)
        else:
            categories[category] = [TreeNode(name)]
    for k, v in categories.items():
        category_node = TreeNode(k)
        root.add_child(category_node)
        for child in v:
            category_node.add_child(child)
    return root