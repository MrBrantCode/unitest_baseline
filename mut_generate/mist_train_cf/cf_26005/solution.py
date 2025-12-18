"""
QUESTION:
Write a function `count_leaves_after_removal` that takes a binary tree and a node to be deleted as input. The function should return the total number of leaf nodes in the binary tree after the node is deleted. Assume the binary tree is represented as a tree where each node has a 'value', 'left', and 'right' attribute.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def count_leaves_after_removal(root, node_to_delete):
    """
    Counts the total number of leaf nodes in the binary tree after a node is deleted.

    Args:
        root (TreeNode): The root of the binary tree.
        node_to_delete (TreeNode): The node to be deleted from the binary tree.

    Returns:
        int: The total number of leaf nodes in the binary tree after the node is deleted.
    """
    def is_leaf(node):
        return node and not node.left and not node.right

    def count_leaves(node):
        if not node:
            return 0
        if is_leaf(node):
            return 1
        return count_leaves(node.left) + count_leaves(node.right)

    def delete_node(node, node_to_delete):
        if not node:
            return None
        if node == node_to_delete:
            if not node.left and not node.right:
                return None
            elif node.left and not node.right:
                return node.left
            elif not node.left and node.right:
                return node.right
            else:
                # Find the minimum node in the right subtree
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.value = min_node.value
                node.right = delete_node(node.right, min_node)
        node.left = delete_node(node.left, node_to_delete)
        node.right = delete_node(node.right, node_to_delete)
        return node

    root = delete_node(root, node_to_delete)
    return count_leaves(root)