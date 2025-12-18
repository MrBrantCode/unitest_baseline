"""
QUESTION:
Implement a function called factorial that calculates the factorial of a given integer using a stack data structure to simulate recursion. The function should not use any built-in recursive functions or loops. The input is a non-negative integer, and the output should be the factorial of the input number.
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0

def factorial(n):
    stack = Stack()
    stack.push(n)
    result = 1

    while not stack.isEmpty():
        num = stack.pop()
        result *= num

        if num > 1:
            stack.push(num - 1)
    
    return result