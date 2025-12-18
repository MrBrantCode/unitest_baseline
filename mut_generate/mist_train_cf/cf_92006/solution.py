"""
QUESTION:
Implement a `Stack` class that uses a Linked List structure to store elements and supports the following methods: `push(data)`, `pop()`, `peek()`, `is_empty()`, `get_size()`, `clear()`, and `get_min()`. The `get_min()` method should return the minimum element in the stack in O(1) time. The `clear()` method should remove all elements from the stack. The `pop()` and `clear()` methods should also update the minimum element accordingly.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def entrance(data):
    class Stack:
        def __init__(self):
            self.head = None
            self.size = 0
            self.min_stack = []

        def push(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

            if not self.min_stack or data <= self.min_stack[-1]:
                self.min_stack.append(data)

        def pop(self):
            if self.is_empty():
                return None

            popped = self.head.data
            self.head = self.head.next
            self.size -= 1

            if popped == self.min_stack[-1]:
                self.min_stack.pop()

            return popped

        def peek(self):
            if self.is_empty():
                return None

            return self.head.data

        def is_empty(self):
            return self.size == 0

        def get_size(self):
            return self.size

        def clear(self):
            self.head = None
            self.size = 0
            self.min_stack = []

        def get_min(self):
            if self.is_empty():
                return None

            return self.min_stack[-1]
    return Stack()