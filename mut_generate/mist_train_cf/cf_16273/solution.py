"""
QUESTION:
Given a binary tree, write a function that prints the binary tree in pre-order traversal and returns the number of nodes in the tree, the sum of all the node values, and the product of all the leaf node values.

The function should operate within the following constraints:
- The function takes the root of the binary tree as input.
- The number of nodes in the tree is between 1 and 10^6.
- The value of each node is between -10^6 and 10^6.
- The space complexity of the function should be O(1).
- The time complexity of the function should be O(N), where N is the number of nodes in the tree.

Note: The binary tree node structure is represented as a class with attributes 'val', 'left', and 'right' representing the node's value and its left and right child nodes, respectively.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def entrance(root):
    """
    Prints the binary tree in pre-order traversal and returns the number of nodes in the tree, 
    the sum of all the node values, and the product of all the leaf node values.

    Args:
    root (TreeNode): The root of the binary tree.

    Returns:
    tuple: A tuple containing the number of nodes, sum of all node values, and product of leaf node values.
    """
    
    # Initialize variables to store the number of nodes, sum of node values, and product of leaf node values
    num_nodes = 0
    sum_node_values = 0
    product_leaf_node_values = 1

    # Define a helper function for pre-order traversal
    def pre_order_helper(node):
        nonlocal num_nodes, sum_node_values, product_leaf_node_values

        # Base case: If the node is None, return
        if node is None:
            return

        # Print the node value in pre-order traversal
        print(node.val, end=" ")

        # Increment the number of nodes and add the node value to the sum
        num_nodes += 1
        sum_node_values += node.val

        # If the node is a leaf node, multiply its value with the product of leaf node values
        if node.left is None and node.right is None:
            product_leaf_node_values *= node.val

        # Recursively traverse the left and right subtrees
        pre_order_helper(node.left)
        pre_order_helper(node.right)

    # Perform pre-order traversal
    pre_order_helper(root)

    # Return the number of nodes, sum of node values, and product of leaf node values
    return num_nodes, sum_node_values, product_leaf_node_values