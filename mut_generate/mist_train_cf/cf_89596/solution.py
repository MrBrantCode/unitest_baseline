"""
QUESTION:
Create a Stack class with a method called `perform_operation` that takes two parameters: `operation` (a string) and `value`. The method should modify the stack based on the value of `operation`. The operation can be either "push", "pop", or "peek". If `operation` is "push", the method should add the `value` to the top of the stack. If `operation` is "pop", the method should remove the top element from the stack. If `operation` is "peek", the method should return the top element from the stack without removing it. If `operation` is anything else, the method should print "Invalid operation". The `perform_operation` method should be implemented in addition to the standard stack methods (`push`, `pop`, `peek`, `is_empty`, `size`).
"""

def perform_operation(stack, operation, value):
    """
    Perform an operation on the stack.

    Args:
    stack (list): The stack to perform the operation on.
    operation (str): The operation to perform. Can be "push", "pop", or "peek".
    value (any): The value to push onto the stack if operation is "push".

    Returns:
    any: The top element of the stack if operation is "peek".
    """
    if operation == "push":
        stack.append(value)
    elif operation == "pop":
        if stack:
            stack.pop()
    elif operation == "peek":
        if stack:
            return stack[-1]
    else:
        print("Invalid operation")