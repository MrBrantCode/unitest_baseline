"""
QUESTION:
Write a function `reverse_linked_list(node, prev=None)` that prints the reversed version of a given linked list without using the built-in reverse() function. The function should have a time complexity of O(n) and space complexity of O(1), where n is the number of nodes in the linked list. The function should work with linked lists containing objects or strings as node values, and it should only use bitwise operations or traditional arithmetic operations for pointer manipulation, without using any additional variables or data structures other than the input linked list itself.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(node, prev=None):
    if node is None:
        return prev
    next_node = node.next
    node.next = prev
    return reverse_linked_list(next_node, node)