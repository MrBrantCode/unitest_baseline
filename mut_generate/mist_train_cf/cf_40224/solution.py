"""
QUESTION:
Implement the `part1` function, which takes a list of instructions as input, where each instruction is either a bitmask assignment (`mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X`) or a memory assignment (`mem[8] = 11`). The function should apply the bitmask to the memory address before writing a value to the memory location and return the sum of all values left in memory after processing all instructions. The bitmask is a 36-bit string of 0s, 1s, and Xs, where 0s and 1s overwrite the corresponding bits in the memory address, and Xs are wildcards that can be either 0 or 1.
"""

import re

def part1(instructions):
    memory = {}
    mask = ''
    for instruction in instructions:
        if instruction.startswith('mask'):
            mask = instruction.split(' = ')[1]
        else:
            address, value = map(int, re.findall(r'\d+', instruction))
            result = ''
            for m, v in zip(mask, format(value, '036b')):
                result += v if m == 'X' else m
            memory[address] = int(result, 2)
    return sum(memory.values())