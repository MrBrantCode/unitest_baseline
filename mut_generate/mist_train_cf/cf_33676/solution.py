"""
QUESTION:
Write a function `compile_to_bytecode` that takes a list of high-level instructions as strings and returns the corresponding bytecode for a custom virtual machine as a list of integers. The virtual machine supports the instructions `PUSH <value>`, `ADD`, `SUB`, `MUL`, `DIV`, and `PRINT` with the following bytecode mappings: `PUSH <value>` maps to the value itself, `ADD` maps to 1, `SUB` maps to 2, `MUL` maps to 3, `DIV` maps to 4, and `PRINT` maps to 5.
"""

def compile_to_bytecode(instructions):
    bytecode = []
    for instruction in instructions:
        parts = instruction.split()
        if parts[0] == "PUSH":
            bytecode.append(int(parts[1]))
        elif parts[0] == "ADD":
            bytecode.append(1)
        elif parts[0] == "SUB":
            bytecode.append(2)
        elif parts[0] == "MUL":
            bytecode.append(3)
        elif parts[0] == "DIV":
            bytecode.append(4)
        elif parts[0] == "PRINT":
            bytecode.append(5)
    return bytecode