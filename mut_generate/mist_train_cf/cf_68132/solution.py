"""
QUESTION:
Write a function named `prune_tree` that takes as input a binary classification tree and a minimum proportion difference threshold (e.g. 5%), and returns the pruned tree. The function should prune the tree such that splits are only kept if the proportion of positive cases differs by more than the specified threshold.
"""

class Node:
    def __init__(self, proportion, left=None, right=None):
        self.proportion = proportion
        self.left = left
        self.right = right

def prune_tree(node, threshold):
    """
    Prune a binary classification tree based on a minimum proportion difference threshold.

    Args:
        node (Node): The root node of the binary classification tree.
        threshold (float): The minimum proportion difference threshold.

    Returns:
        Node: The pruned tree.
    """
    if node is None:
        return None

    node.left = prune_tree(node.left, threshold)
    node.right = prune_tree(node.right, threshold)

    if node.left is not None and node.right is not None:
        # Compute the proportion if the current node and its sibling are collapsed into their parent.
        collapsed_proportion = (node.left.proportion + node.right.proportion) / 2

        # Check if the resulting proportions don't differ by more than the threshold.
        if abs(node.left.proportion - collapsed_proportion) <= threshold and abs(node.right.proportion - collapsed_proportion) <= threshold:
            # Collapse the nodes by returning the parent node with the collapsed proportion.
            return Node(collapsed_proportion)

    return node