"""
QUESTION:
Write a method named `length_link` and `sum_link` that takes the head of a singly linked list as input and returns both the length of the linked list and the sum of all the values in the linked list. The linked list is represented by instances of a class named `Node`, each carrying a numeric value and connecting to the subsequent `Node`. The `Node` class has two attributes: `val` and `next`, where `val` is the value of the node and `next` is a reference to the next node in the list. The methods should traverse the linked list and return the required information.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def length_link(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length

def sum_link(node):
    total = 0
    while node:
        total += node.val
        node = node.next
    return total