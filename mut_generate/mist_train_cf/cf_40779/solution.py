"""
QUESTION:
Implement the `execute` function that takes an instruction, the current register state, and the program counter as input. The function should return the updated register state, the final program counter, and a string representing the execution result. The instruction set includes ADD, SUB, and MOV. The `execute` function should update the register state and program counter accordingly for each instruction type.
"""

def execute(instruction, register_state, program_counter):
    if instruction.startswith('ADD'):
        operands = instruction.split(' ')[1:]
        reg1, reg2, reg3 = operands
        register_state[reg1] = register_state[reg2] + register_state[reg3]
        program_counter += 1
        return register_state, program_counter, f'Added {register_state[reg2]} and {register_state[reg3]}'

    elif instruction.startswith('SUB'):
        operands = instruction.split(' ')[1:]
        reg1, reg2, reg3 = operands
        register_state[reg1] = register_state[reg2] - register_state[reg3]
        program_counter += 1
        return register_state, program_counter, f'Subtracted {register_state[reg3]} from {register_state[reg2]}'

    elif instruction.startswith('MOV'):
        operands = instruction.split(' ')[1:]
        reg1, reg2 = operands
        register_state[reg1] = register_state[reg2]
        program_counter += 1
        return register_state, program_counter, f'Moved {register_state[reg2]} to {reg1}'