"""
QUESTION:
Implement the function `execute_mips_instructions(instructions)` that simulates the execution of a list of MIPS assembly instructions and returns the final state of the MIPS registers as a dictionary. The function should execute each instruction in the order they appear in the list and update the MIPS registers accordingly. The MIPS architecture uses 32 general-purpose registers labeled `$0` to `$31`. The `instructions` parameter is a list of strings, where each string represents a single MIPS assembly instruction.
"""

def execute_mips_instructions(instructions):
    registers = {f"${i}": 0 for i in range(32)}  
    memory = {}  # Simulated memory
    for instruction in instructions:
        parts = instruction.split()
        opcode = parts[0]
        if opcode == "add":
            dest_reg, src_reg1, src_reg2 = parts[1], parts[2], parts[3]
            registers[dest_reg] = registers[src_reg1] + registers[src_reg2]
        elif opcode == "lw":
            dest_reg, offset, base_reg = parts[1], int(parts[2].split('(')[0]), parts[2].split('(')[1][:-1]
            registers[dest_reg] = memory.get(registers[base_reg] + offset, 0)  
        elif opcode == "sw":
            src_reg, offset, base_reg = parts[1], int(parts[2].split('(')[0]), parts[2].split('(')[1][:-1]
            memory[registers[base_reg] + offset] = registers[src_reg]  
    return registers