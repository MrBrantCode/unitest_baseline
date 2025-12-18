"""
QUESTION:
Find the value of the accumulator when a program terminates. The program is represented as a list of instructions, where each instruction is either "acc x" to increase the accumulator by x, "jmp x" to jump to a new instruction relative to the current one, or "nop" to proceed to the next instruction. The program terminates when an instruction is about to be executed a second time.

Write a function `find_accumulator_value(instructions: List[str]) -> int` that takes in the list of instructions and returns the value of the accumulator when the program terminates.
"""

from typing import List

def entrance(instructions: List[str]) -> int:
    acc = 0
    done = [False] * len(instructions)
    i = 0

    while i < len(instructions):
        if done[i]:
            break  
        done[i] = True  

        instruction, *value = instructions[i].split()
        value = int(value[0] if value else 0)

        if instruction == "acc":
            acc += value
            i += 1
        elif instruction == "jmp":
            i += value
        else:  
            i += 1

    return acc