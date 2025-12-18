"""
QUESTION:
Implement a `perform_operation` function for a stack data structure that takes an extra `operation` parameter, which can be "push", "pop", or "peek", and performs the corresponding operation on the stack. The function should also take an extra `value` parameter that is used when the operation is "push".
"""

def entance(stack, operation, value):
    if operation == "push":
        stack.append(value)
    elif operation == "pop":
        if stack:
            stack.pop()
    elif operation == "peek":
        if stack:
            return stack[-1]
        return None
    else:
        return "Invalid operation"