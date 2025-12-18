"""
QUESTION:
Implement a function `array_stack_operations` that uses a fixed-size array to store stack elements and performs push, pop, and peek operations. The function should keep track of the last element added to the stack using an index variable and maintain a fixed-size array. Analyze the time complexity for push, pop, and peek operations, and the space complexity of the array-based stack. Assume the maximum capacity of the stack is n.
"""

class ArrayStack:
    def __init__(self, n):
        self.stack = [None] * n
        self.top = -1
        self.max_size = n

    def push(self, x):
        """Adds an element to the top of the stack."""
        if self.top < self.max_size - 1:
            self.top += 1
            self.stack[self.top] = x
        else:
            raise Exception("Stack is full")

    def pop(self):
        """Removes an element from the top of the stack."""
        if self.top >= 0:
            x = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return x
        else:
            raise Exception("Stack is empty")

    def peek(self):
        """Returns the top element of the stack without removing it."""
        if self.top >= 0:
            return self.stack[self.top]
        else:
            raise Exception("Stack is empty")

    def array_stack_operations(self, operations, values):
        result = []
        for i, op in enumerate(operations):
            if op == "push":
                self.push(values[i])
            elif op == "pop":
                result.append(self.pop())
            elif op == "peek":
                result.append(self.peek())
        return result

def array_stack_operations(operations, values, n):
    stack = ArrayStack(n)
    return stack.array_stack_operations(operations, values)