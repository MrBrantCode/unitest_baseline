"""
QUESTION:
Create a function `parse_assembly_instructions` that takes a string of x86-64 assembly instructions as input, where each instruction is separated by a semicolon. The function should parse and interpret the instructions to extract the operations being performed and the operands involved. The function should return a list of tuples, where each tuple contains the operation and operands for each instruction.
"""

import re

def parse_assembly_instructions(assembly_code):
    """
    This function takes a string of x86-64 assembly instructions as input, 
    parses and interprets the instructions to extract the operations being 
    performed and the operands involved, and returns a list of tuples, 
    where each tuple contains the operation and operands for each instruction.

    Args:
        assembly_code (str): A string of x86-64 assembly instructions.

    Returns:
        list: A list of tuples containing the operation and operands for each instruction.
    """
    parsed_instructions = []
    for instruction in assembly_code.split(';'):
        instruction = instruction.strip()
        if instruction:
            operation = re.search(r'(\w+)\s(.+)', instruction).group(1)
            operands = re.search(r'(\w+)\s(.+)', instruction).group(2)
            parsed_instructions.append((operation, operands))
    return parsed_instructions