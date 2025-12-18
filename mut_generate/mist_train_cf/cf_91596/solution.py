"""
QUESTION:
Create a function `print_reverse` that takes the head of a singly linked list as input and prints the elements of the list in reverse order without using any additional data structures or extra space. The function should recursively traverse the linked list and print the elements in reverse order.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_reverse(node):
    if node is None:
        return
    print_reverse(node.next)
    print(node.data, end=' ')