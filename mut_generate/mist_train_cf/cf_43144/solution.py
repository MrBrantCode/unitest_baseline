"""
QUESTION:
Implement a function `process_instructions(instructions: List[str], registers: Dict[str, int]) -> Dict[str, int]`. This function processes a list of instructions and updates a dictionary of registers based on the instructions. The instructions can be in four formats: `incRegister` to increment a register, `decRegister` to decrement a register, `jnzRegisterValue` to jump to a line if a register's value is not zero, and `jnzRegisterRegister` to jump to a line if the first register's value is not zero. The function returns the updated registers dictionary. Assume the input instructions are well-formed and the registers dictionary contains valid register names.
"""

import re
from typing import List, Dict

def process_instructions(instructions: List[str], registers: Dict[str, int]) -> Dict[str, int]:
    i = 0
    while i < len(instructions):
        line = instructions[i]
        m1 = re.search(r'inc (\w+)', line)
        if m1:
            register = m1.group(1)
            registers[register] += 1
            i += 1
            continue

        m2 = re.search(r'dec (\w+)', line)
        if m2:
            register = m2.group(1)
            registers[register] -= 1
            i += 1
            continue

        m3 = re.search(r'jnz (\w+) (-?\d+)', line)
        if m3:
            (register, jump) = m3.groups()
            if registers[register] != 0:
                i += int(jump)
            else:
                i += 1
            continue

        m4 = re.search(r'jnz (\w+) (\w+)', line)
        if m4:
            (tester, jump) = m4.groups()
            if registers[tester] != 0:
                i += registers[jump]
            else:
                i += 1
            continue

    return registers