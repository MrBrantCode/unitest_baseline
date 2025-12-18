"""
QUESTION:
Write a function `compile` that takes a list of instruction strings as input, where each instruction consists of an operation followed by operands, and returns the compiled machine code as a string. The operations supported are "ADD", "SUB", "MUL", and "DIV", and the operands are integers. The compiled machine code should be a sequence of operations and operands separated by spaces.
"""

def compile(instructions):
    machine_code = ' '.join(instructions)
    return machine_code