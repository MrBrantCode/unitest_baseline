"""
QUESTION:
Implement a function `redasm_interpreter` that takes a list of strings representing REDASM instructions and returns the final state of the stack after executing all the instructions. The function should support the following instructions: 
- `PUSH <value>`: Pushes the integer value onto the stack.
- `POP`: Removes the top element from the stack.
- `ADD`: Pops the top two elements from the stack, adds them, and pushes the result back onto the stack.
- `SUB`: Pops the top two elements from the stack, subtracts the top element from the second, and pushes the result back onto the stack.
- `MUL`: Pops the top two elements from the stack, multiplies them, and pushes the result back onto the stack.
- `DIV`: Pops the top two elements from the stack, divides the second element by the top element, and pushes the result back onto the stack. If the top element is 0, the function should return -1.
 
If an instruction encounters an error (e.g., popping from an empty stack, division by zero), the function should terminate and return -1. The stack is initially empty and can hold integers.
"""

from typing import List

def redasm_interpreter(instructions: List[str]) -> int:
    stack = []
    for instruction in instructions:
        if instruction.startswith("PUSH"):
            value = int(instruction.split()[1])
            stack.append(value)
        elif instruction == "POP":
            if stack:
                stack.pop()
            else:
                return -1  
        elif instruction == "ADD":
            if len(stack) >= 2:
                stack.append(stack.pop() + stack.pop())
            else:
                return -1  
        elif instruction == "SUB":
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            else:
                return -1  
        elif instruction == "MUL":
            if len(stack) >= 2:
                stack.append(stack.pop() * stack.pop())
            else:
                return -1  
        elif instruction == "DIV":
            if len(stack) >= 2:
                divisor = stack.pop()
                if divisor == 0:
                    return -1  
                dividend = stack.pop()
                stack.append(dividend // divisor)
            else:
                return -1  
    return stack[-1] if stack else 0  