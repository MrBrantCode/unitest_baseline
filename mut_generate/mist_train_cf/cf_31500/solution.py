"""
QUESTION:
Implement a function `final_stack_state(operations)` that simulates a stack based on a given list of operations and returns the final state of the stack. The operations can be one of the following:
- "PUSH X": Push the integer X onto the stack.
- "POP": Pop the top element from the stack.
- "INC Y Z": Increment the bottom Y elements of the stack by Z.

The function should handle these operations in the given order and return the final state of the stack as a list. The input is a list of strings representing the operations.
"""

def final_stack_state(operations):
    stack = []
    for op in operations:
        if op.startswith("PUSH"):
            _, num = op.split()
            stack.append(int(num))
        elif op == "POP":
            stack.pop()
        elif op.startswith("INC"):
            _, y, z = op.split()
            y, z = int(y), int(z)
            for i in range(min(y, len(stack))):
                stack[i] += z
    return stack