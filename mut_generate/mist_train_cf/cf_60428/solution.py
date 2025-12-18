"""
QUESTION:
Write a function `compute_arithmetic_seq` that takes two lists as input: `operator_set` and `operand_set`. `operator_set` contains basic arithmetic operations as strings and `operand_set` contains positive integers. The length of `operator_set` is always one less than the length of `operand_set`. The function should construct and evaluate a mathematical expression using the given operators and operands, returning the final result.
"""

def compute_arithmetic_seq(operator_set, operand_set):
    # Initialize final result with the first operand
    result = operand_set[0]
    
    # Map string operator to actual operator
    operator_mapping = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y
    }
    
    # Iterate through the rest of the operands and apply the corresponding operator
    for i in range(1, len(operand_set)):
        operator = operator_mapping[operator_set[i-1]]
        result = operator(result, operand_set[i])
    
    return result