"""
QUESTION:
Implement a Stack data structure with error handling for stack overflow situations. The function should include the following methods: push, pop, is_empty, and peek. The stack should be initialized with a maximum size and should not crash when this size is exceeded. Instead, it should print an error message indicating that the item cannot be pushed to the stack.
"""

def entrance(max_size):
    class Stack:
        def __init__(self):
            self.max_size = max_size
            self.stack = []

        def push(self, item):
            if len(self.stack) >= self.max_size:
                print("Stack overflow! Cannot push item:", item)
            else:
                self.stack.append(item)

        def pop(self):
            if len(self.stack) == 0:
                print("Stack is empty!")
            else:
                return self.stack.pop()

        def is_empty(self):
            return len(self.stack) == 0

        def peek(self):
            if len(self.stack) == 0:
                print("Stack is empty!")
            else:
                return self.stack[-1]

    return Stack()