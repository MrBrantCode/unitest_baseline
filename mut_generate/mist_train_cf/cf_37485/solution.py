"""
QUESTION:
Implement the `performOperations(operations)` function, which takes a list of strings representing stack operations as input and returns the final state of the stack. The operations can be "push n" to push an integer onto the stack, "pop" to remove the top element, or "inc i v" to add v to the first i elements. The function should handle each operation accordingly and return the resulting stack.
"""

from typing import List

def performOperations(operations: List[str]) -> List[int]:
    stack = []
    for op in operations:
        if op.startswith("push"):
            _, num = op.split()
            stack.append(int(num))
        elif op == "pop":
            stack.pop()
        elif op.startswith("inc"):
            _, i, v = op.split()
            i, v = int(i), int(v)
            for j in range(min(i, len(stack))):
                stack[j] += v
    return stack