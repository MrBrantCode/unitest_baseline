"""
QUESTION:
Write a function `count_twigs(tree)` that takes an n-ary tree as input and returns the number of twig nodes present in the tree. A twig node is a node with no child nodes. The function should work for any generic representation of an n-ary tree, where each node is represented as a dictionary with a "data" key and an optional "children" key containing a list of child nodes. The function should not have any hardcoded structure specificity.
"""

def count_twigs(tree):
    if "children" not in tree or not tree["children"]:
        return 1
    else:
        cnt = 0
        for child in tree["children"]:
            cnt += count_twigs(child)
        return cnt