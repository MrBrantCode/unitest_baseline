"""
QUESTION:
Implement a function `detectThreats` that takes in a list of instructions, where each instruction is a string in the format "operation register value". The operation can be "MOV", "ADD", "SUB", or "CMP", the register is a single uppercase letter from 'A' to 'Z', and the value can be either a hexadecimal number prefixed with "0x" or a decimal number. Return a list of indices (0-based) where potential security threats are detected, which occurs when the operation is "CMP" and the comparison involves the bitwise AND operation between the value of a specific register and a hexadecimal number derived from another instruction.
"""

def detect_threats(instruction_list):
    threats = []
    registers = [0] * 26  # Initialize registers A-Z with 0
    for i in range(len(instruction_list)):
        operation, register, value = instruction_list[i].split()
        if operation == "MOV":
            registers[ord(register) - ord('A')] = int(value, 16) if value.startswith("0x") else int(value)
        elif operation == "CMP":
            x = int(value, 16)
            if registers[ord(register) - ord('A')] & x != x:
                threats.append(i)
    return threats