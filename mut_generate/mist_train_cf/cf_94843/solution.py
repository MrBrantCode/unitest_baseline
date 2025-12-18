"""
QUESTION:
Implement a function called `reverse` to reverse the contents of a stack without using any additional data structures. The function should have a time complexity of O(n), where n is the size of the stack.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def insert_at_bottom(self, data):
        if self.top is None:
            self.push(data)
        else:
            temp = self.pop()
            self.insert_at_bottom(data)
            self.push(temp)

def reverse(stack):
    if stack.top is None:
        return
    data = stack.pop()
    reverse(stack)
    stack.insert_at_bottom(data)