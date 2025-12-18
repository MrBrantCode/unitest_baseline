"""
QUESTION:
Write a function called `print_tree` that takes a tree structure as input, where the tree is represented as a list of tuples, and each tuple contains a node value and a list of its children. The function should print the tree structure with indentation to indicate the level of each node and include the number of descendants for each node. The input tree can have up to 10,000 nodes.
"""

def print_tree(tree, level=0):
    if not tree:
        return
    
    value, children = tree
    num_descendants = count_descendants(children)
    
    print("{}{} ({})".format("\t" * level, value, num_descendants))
    
    for child in children:
        print_tree(child, level+1)

def count_descendants(children):
    count = len(children)
    
    for child in children:
        count += count_descendants(child[1])
    
    return count