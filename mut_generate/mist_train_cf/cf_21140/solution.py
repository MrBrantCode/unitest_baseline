"""
QUESTION:
Implement a function `print_tree` that takes a tree structure represented as a tuple containing a node value and a list of its children, and prints the tree structure with parent-child relationships, indentation indicating node levels, and the number of descendants for each node. 

The function should handle a tree structure represented as a list of tuples, where each tuple contains a node value and a list of its children, and each child is also a tuple. The function should print each node value followed by its number of descendants in parentheses, with indentation representing the node's level in the tree. 

The input tree structure is a list of tuples, where each tuple contains two elements: a node value (a string) and a list of its children (a list of tuples). The function should not take any other inputs or parameters.
"""

def print_tree(node):
    def count_descendants(children):
        descendants = len(children)
        for child in children:
            descendants += count_descendants(child[1])
        return descendants

    def recursive_print(node, level):
        indent = "    " * level
        descendants = count_descendants(node[1])
        print(f"{indent}{node[0]} ({descendants})")
        for child in node[1]:
            recursive_print(child, level + 1)

    recursive_print(node, 0)