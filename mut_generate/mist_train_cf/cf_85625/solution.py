"""
QUESTION:
Implement a function `sort_and_reverse_print` that sorts a linked list in ascending order and then prints it in reverse order without using any built-in sort or reverse functions. The function should only use a Stack as an auxiliary data structure. The input is the head node of the linked list, and the output is the reversed and sorted linked list. The function should modify the original linked list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.value

def insert_sorted(node, value):
    if node is None or node.value > value:
        new_node = Node(value)
        new_node.next = node
        return new_node
    else:
        node.next = insert_sorted(node.next, value)
        return node

def sort_and_reverse_print(node):
    current = node
    new_head = None
    while current is not None:
        new_head = insert_sorted(new_head, current.value)
        current = current.next

    stack = Stack()
    while new_head is not None:
        stack.push(new_head.value)
        new_head = new_head.next

    while not stack.is_empty():
        print(stack.pop())