"""
QUESTION:
Write a function `resolve_data_hazard` that takes as input a list of instructions and resolves any data hazards that may occur due to read-after-write (RAW) dependencies. The function should use forwarding, stalling, or speculative execution to resolve the hazards. The function should return the resolved list of instructions.

The input list of instructions is in the format of a list of tuples, where each tuple contains the instruction type, destination register, and source registers. For example: [("ADD", "R1", "R2", "R3"), ("SUB", "R4", "R1", "R5")].
"""

def resolve_data_hazard(instructions):
    """
    Resolves data hazards in a list of instructions due to read-after-write (RAW) dependencies.

    Args:
        instructions (list): A list of tuples, where each tuple contains the instruction type, 
            destination register, and source registers.

    Returns:
        list: The resolved list of instructions.
    """

    # Create a dictionary to keep track of the last instruction that wrote to each register
    last_write = {}

    # Initialize an empty list to store the resolved instructions
    resolved_instructions = []

    # Iterate over each instruction in the input list
    for instruction in instructions:
        # Extract the instruction type, destination register, and source registers
        inst_type, dest, src1, src2 = instruction

        # Check if the instruction has any RAW dependencies
        if src1 in last_write or src2 in last_write:
            # If there is a RAW dependency, stall the instruction by inserting a NOP
            resolved_instructions.append(("NOP",))
        else:
            # If there is no RAW dependency, add the instruction to the resolved list
            resolved_instructions.append(instruction)

            # Update the last_write dictionary if the instruction writes to a register
            if inst_type in ["ADD", "SUB", "MUL"]:
                last_write[dest] = instruction

    return resolved_instructions