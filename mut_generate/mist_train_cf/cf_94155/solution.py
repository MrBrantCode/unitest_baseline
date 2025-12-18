"""
QUESTION:
Write a function named `pre_order_traversal` that prints a binary tree in pre-order traversal and returns the number of nodes, sum of all node values, and product of all leaf node values. 

The binary tree is defined by the class `TreeNode`, where each node contains an integer value and references to its left and right children. The function should have a space complexity of O(1) and a time complexity of O(N), where N is the number of nodes in the tree. The function should be able to handle trees with between 1 and 10^6 nodes, and node values between -10^6 and 10^6.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order_traversal(root):
    """
    Prints a binary tree in pre-order traversal, counts the number of nodes, 
    calculates the sum of all node values, and calculates the product of leaf node values.

    Args:
        root (TreeNode): The root of the binary tree.

    Returns:
        tuple: A tuple containing the number of nodes, sum of all node values, and product of leaf node values.
    """
    if root is None:
        return 0, 0, 1  # Return 1 as the product of leaf nodes for empty tree

    # Initialize variables to store the count, sum, and product
    count = 1
    total_sum = root.val
    product = 1

    # Check if the current node is a leaf node
    if root.left is None and root.right is None:
        product = root.val
    else:
        # Recursively traverse the left subtree
        left_count, left_sum, left_product = pre_order_traversal(root.left)
        count += left_count
        total_sum += left_sum
        product *= left_product

        # Recursively traverse the right subtree
        right_count, right_sum, right_product = pre_order_traversal(root.right)
        count += right_count
        total_sum += right_sum
        product *= right_product

    print(root.val, end=" ")  # Print the current node value
    return count, total_sum, product