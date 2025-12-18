"""
QUESTION:
Implement a function `process_sequence(sequence: str) -> List[str]` that processes a sequence of lowercase alphabet characters and performs the following operations: 
- If a character is not already present in the stack, it should be added to the top of the stack.
- If a character is already present in the stack, it should be removed from the stack.
The function should return the final state of the stack after processing the entire sequence of characters.
"""

from typing import List

def process_sequence(sequence: str) -> List[str]:
    stack = []
    for c in sequence:
        if c not in stack:
            stack.append(c)
        else:
            stack.remove(c)
    return stack