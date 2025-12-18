"""
QUESTION:
Create a function `binary_op` that takes three parameters: an integer `val`, a binary operation `op` (one of 'OR', 'AND', 'XOR', 'SHL', 'SHR'), and an integer operand. The function should convert `val` to binary, perform the binary operation with the operand, and return the result as both a binary string and an integer. The function should be optimized for time efficiency and return an error message if the operation is invalid.
"""

def binary_op(val, op, operand):
    # Dictionary of binary operations
    bin_ops = {
        'AND': lambda x, y: x & y,
        'OR': lambda x, y: x | y,
        'XOR': lambda x, y: x ^ y,
        'SHL': lambda x, y: x << y,
        'SHR': lambda x, y: x >> y,
    }

    # Check if the operation is valid
    if op not in bin_ops:
        return "Invalid operation"

    # Convert to binary and perform operation
    result = bin_ops[op](val, operand)

    # Return binary and integer representation of result
    return (bin(result)[2:], result)