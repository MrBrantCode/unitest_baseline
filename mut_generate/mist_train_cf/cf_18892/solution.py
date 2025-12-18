"""
QUESTION:
Implement a function `factorial(num)` that calculates the factorial of a given number `num` using a stack data structure to simulate recursion. The function should not use any built-in recursive functions or loops and should raise an exception if `num` is a negative number.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def factorial(num):
    if num < 0:
        raise Exception("Factorial is not defined for negative numbers")
    if num == 0:
        return 1

    stack = Stack()
    stack.push(num)

    result = 1
    while not stack.is_empty():
        current_num = stack.pop()
        result *= current_num

        if current_num > 1:
            stack.push(current_num - 1)

    return result