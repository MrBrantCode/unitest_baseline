"""
QUESTION:
Implement the function `generate_burg_rules(ast)` that takes an Abstract Syntax Tree (AST) as input and returns a list of BURG rules for instruction selection. The AST is a tree structure where each node contains information about an operation or expression in the source code. Each BURG rule is a tuple in the format `(pattern, cost, action)`, where the pattern describes the structure of the AST nodes to be matched, the cost represents the expense of using the rule, and the action specifies the machine instructions to be emitted.
"""

def generate_burg_rules(ast):
    rules = []

    def traverse(node):
        if node.type == 'ADD':
            pattern = ('ADD', 1, f'ADD R{node.result}, R{node.left}, R{node.right}')
            rules.append(pattern)
        elif node.type == 'MUL':
            pattern = ('MUL', 1, f'MUL R{node.result}, R{node.left}, R{node.right}')
            rules.append(pattern)

        for child in node.children:
            traverse(child)

    traverse(ast)
    return rules