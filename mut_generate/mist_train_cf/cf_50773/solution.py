"""
QUESTION:
Create a function `create_syntax_tree` to generate a syntax tree for a given mathematical expression. The function should represent the expression as a tree where operators are nodes and operands are leaves, following the order of operations (PEMDAS/BODMAS). The input will be a string representing a simple arithmetic expression containing single-digit numbers and basic arithmetic operators (+, -, *, /). The output should be a text representation of the syntax tree.
"""

def create_syntax_tree(expression):
    # Stack to store operators
    operator_stack = []
    # Stack to store the syntax tree
    syntax_tree_stack = []
    
    # Precedence of operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # Iterate through the expression
    for char in expression:
        # If the character is a digit, add it to the syntax tree stack
        if char.isdigit():
            syntax_tree_stack.append(char)
        # If the character is an operator
        elif char in precedence:
            # Pop operators from the operator stack and add them to the syntax tree stack
            # until an operator with lower precedence is found or the stack is empty
            while operator_stack and precedence[operator_stack[-1]] >= precedence[char]:
                op = operator_stack.pop()
                # Create a tree node with the operator and the last two elements from the syntax tree stack
                right = syntax_tree_stack.pop()
                left = syntax_tree_stack.pop()
                syntax_tree_stack.append(f'({op} {left} {right})')
            # Push the current operator to the operator stack
            operator_stack.append(char)
    
    # Pop any remaining operators from the operator stack and add them to the syntax tree stack
    while operator_stack:
        op = operator_stack.pop()
        # Create a tree node with the operator and the last two elements from the syntax tree stack
        right = syntax_tree_stack.pop()
        left = syntax_tree_stack.pop()
        syntax_tree_stack.append(f'({op} {left} {right})')
    
    # The final syntax tree is the only element in the syntax tree stack
    return syntax_tree_stack[0]