"""
QUESTION:
Write a function `execute_instructions(insts)` that simulates the execution of the given assembly-like instructions and returns the final state of the registers after all instructions have been executed. The instructions are in the form of a 2D array `insts` where each sub-array represents an instruction with the instruction name as the first element and subsequent elements as parameters. The function should initialize registers 'a' to 'z' to 0 before executing the instructions. 

Available instructions are: 
- `cpy x y`: Copies the value of register or integer `x` into register `y`.
- `inc x`: Increases the value of register `x` by 1.
- `dec x`: Decreases the value of register `x` by 1.
- `mul x y z`: Multiplies the values in registers `x` and `y`, and stores the result in register `z`.
- `jnz x y`: Jumps to an instruction `y` away if the value of register `x` is not zero.

Function Signature: `def execute_instructions(insts: List[List[str]]) -> Dict[str, int]`
"""

from typing import List, Dict

def get_value(param: str, r: Dict[str, int]) -> int:
    if param.isdigit() or (param[0] == '-' and param[1:].isdigit()):
        return int(param)
    else:
        return r[param]

def execute_instructions(insts: List[List[str]]) -> Dict[str, int]:
    r = {chr(i): 0 for i in range(97, 123)}  # Initialize registers a-z to 0
    p = 0  # Program counter
    while p < len(insts):
        inst = insts[p][0]
        if inst == 'cpy':
            r[insts[p][2]] = get_value(insts[p][1], r)
        elif inst == 'dec':
            r[insts[p][1]] -= 1
        elif inst == 'inc':
            r[insts[p][1]] += 1
        elif inst == 'mul':
            r[insts[p][3]] += get_value(insts[p][1], r) * get_value(insts[p][2], r)
        elif inst == 'jnz':
            if get_value(insts[p][1], r) != 0:
                p += get_value(insts[p][2], r) - 1
        p += 1
    return r