"""
QUESTION:
Implement a stack data structure called MinStack that supports the following operations in constant time (O(1)): push, pop, top, and getMinimum. The stack should be able to store a large amount of generic data (not just integers) without causing memory issues. The 'top' operation should return the topmost element without removing it, and the 'getMinimum' operation should return the minimum element in the stack without removing it. If the stack is empty, 'pop', 'top', and 'getMinimum' should return an error message instead of giving an error.
"""

def minStack(self, ops):
    class MinStack:
        def __init__(self):
            self.data = []
            self.mins = []

        def push(self, x):
            self.data.append(x)
            if self.mins:
                self.mins.append(min(x, self.mins[-1]))
            else:
                self.mins.append(x)

        def pop(self):
            if not self.data:
                return "Stack is empty"
            self.mins.pop()
            return self.data.pop()

        def top(self):
            if not self.data:
                return "Stack is empty"
            return self.data[-1]

        def getMinimum(self):
            if not self.mins:
                return "Stack is empty"
            return self.mins[-1]