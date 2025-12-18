"""
QUESTION:
Implement a function named `disassemble_instruction` that takes a 32-bit machine code instruction as input and returns its corresponding assembly language mnemonic. The opcode field is the first 6 bits of the instruction. The function should support at least 5 different instructions, handle unknown opcodes, and return "UNKNOWN" for invalid instructions.
"""

def disassemble_instruction(instruction):
    opcode = instruction >> 26  # Extracting the opcode from the instruction
    if opcode == 0b000000:
        return "ADD"  # Opcode 0b000000 corresponds to the ADD instruction
    elif opcode == 0b000010:
        return "SUB"  # Opcode 0b000010 corresponds to the SUB instruction
    elif opcode == 0b001000:
        return "ADDI"  # Opcode 0b001000 corresponds to the ADDI instruction
    elif opcode == 0b100011:
        return "LW"  # Opcode 0b100011 corresponds to the LW instruction
    elif opcode == 0b101011:
        return "SW"  # Opcode 0b101011 corresponds to the SW instruction
    else:
        return "UNKNOWN"  # Handle unknown opcodes