"""
QUESTION:
Implement a class `MinStack` with methods `__init__`, `push(val)`, `pop()`, and `get_min()`. The class should support a stack data structure with the following operations: 
- `__init__`: Initializes an empty stack.
- `push(val)`: Adds the element `val` to the top of the stack.
- `pop()`: Removes the top element from the stack and returns it.
- `get_min()`: Returns the minimum element in the stack without removing it.

All operations should run in O(1) time complexity.
"""

def minStackOperations(val=None, operation=None, minStack=None):
    if minStack is None:
        minStack = {"stack": [], "min_stack": []}

    if operation == "push":
        minStack["stack"].append(val)
        if not minStack["min_stack"] or val <= minStack["min_stack"][-1]:
            minStack["min_stack"].append(val)
    elif operation == "pop":
        if minStack["stack"]:
            if minStack["stack"][-1] == minStack["min_stack"][-1]:
                minStack["min_stack"].pop()
            minStack["stack"].pop()
    elif operation == "get_min":
        if minStack["min_stack"]:
            return minStack["min_stack"][-1]

    return minStack