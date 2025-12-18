"""
QUESTION:
Implement a function `process_conditionals(code)` that processes a list of conditional statements and returns the order in which the code blocks should be executed. The function should follow these rules:
- When an "if" statement is encountered, push "if" onto the stack.
- When an "elseif" statement is encountered, pop the top element from the stack and push "elseif" onto the stack.
- When an "else" statement is encountered, directly execute the associated code block without pushing anything onto the stack.
The input `code` is a list of strings, each representing a line of code, with at most 1000 elements and a maximum length of 100 characters.
"""

from typing import List

def process_conditionals(code: List[str]) -> str:
    stack = []
    for line in code:
        if line.startswith('if'):
            stack.append('if')
        elif line.startswith('elseif'):
            stack.pop(-1)
            stack.append('elseif')
        elif line.startswith('else'):
            pass
    return_code = ""
    for line in code:
        if line.startswith('if'):
            return_code += line.split(':')[1].strip() + "\n"
        elif line.startswith('elseif'):
            return_code += line.split(':')[1].strip() + "\n"
        elif line.startswith('else'):
            return_code += line.split(':')[1].strip() + "\n"
    return return_code.strip()