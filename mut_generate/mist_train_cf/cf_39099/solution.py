"""
QUESTION:
Implement a function `execute_program` that simulates the execution of a simple assembly-like language. The function takes a list of instructions as input, where each instruction is a tuple containing an operation and three integer arguments. The function should return the value of register 0 when the program first tries to run an instruction with the instruction pointer equal to the value in the `ip_reg` register for the second time. The `ip_reg` register is assumed to be register 4. The available operations are "addr", "addi", "mulr", "muli", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", and "eqrr".
"""

def execute_program(instructions: list) -> int:
    ip_reg = 4
    reg = [0, 0, 0, 0, 0, 0]
    i = 0
    seen = set()

    while reg[ip_reg] < len(instructions):
        if reg[ip_reg] == 1:
            if reg[0] in seen:
                return reg[0]
            seen.add(reg[0])

        op, a, b, c = instructions[reg[ip_reg]]
        if op == "addr":
            reg[c] = reg[a] + reg[b]
        elif op == "addi":
            reg[c] = reg[a] + b
        elif op == "mulr":
            reg[c] = reg[a] * reg[b]
        elif op == "muli":
            reg[c] = reg[a] * b
        elif op == "setr":
            reg[c] = reg[a]
        elif op == "seti":
            reg[c] = a
        elif op == "gtir":
            reg[c] = 1 if a > reg[b] else 0
        elif op == "gtri":
            reg[c] = 1 if reg[a] > b else 0
        elif op == "gtrr":
            reg[c] = 1 if reg[a] > reg[b] else 0
        elif op == "eqir":
            reg[c] = 1 if a == reg[b] else 0
        elif op == "eqri":
            reg[c] = 1 if reg[a] == b else 0
        elif op == "eqrr":
            reg[c] = 1 if reg[a] == reg[b] else 0

        reg[ip_reg] += 1

    return reg[0]