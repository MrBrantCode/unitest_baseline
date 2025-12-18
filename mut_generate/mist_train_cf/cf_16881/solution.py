"""
QUESTION:
Create a recursive function named `create_expression_tree` that constructs an expression tree for a given mathematical expression. The function should take a string expression as input, where the expression only contains single-digit numbers and the operators '+', '-', '*', '/'. The function should return the root node of the constructed expression tree. The expression tree should be represented as a binary tree where internal nodes are operators and leaf nodes are operands.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_expression_tree(expression):
    """
    Creates an expression tree for a given mathematical expression.

    Args:
    expression (str): A string expression containing single-digit numbers and operators '+', '-', '*', '/'.

    Returns:
    TreeNode: The root node of the constructed expression tree.
    """

    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Convert the expression into a list of operators and operands
    tokens = []
    for char in expression:
        if char in precedence:
            tokens.append(char)
        else:
            tokens.append(int(char))

    # Create a helper function to construct the expression tree recursively
    def construct_tree(tokens):
        # Base case: if the list of tokens is empty, return None
        if not tokens:
            return None

        # Find the operator with the lowest precedence
        min_precedence = float('inf')
        min_index = -1
        for i, token in enumerate(tokens):
            if token in precedence and precedence[token] < min_precedence:
                min_precedence = precedence[token]
                min_index = i

        # If no operator is found, the expression is a single operand
        if min_index == -1:
            node = TreeNode(tokens[0])
            return node

        # Create a new node with the operator
        node = TreeNode(tokens[min_index])

        # Recursively construct the left and right subtrees
        node.left = construct_tree(tokens[:min_index])
        node.right = construct_tree(tokens[min_index + 1:])

        return node

    # Call the helper function to construct the expression tree
    return construct_tree(tokens)