"""
QUESTION:
Write a function named `reverse_list_recursively` that takes two parameters, `curr` (the current node) and `prev` (the previous node), to reverse a linked list without using any built-in functions or data structures, without using any loops, and with a time complexity of O(n), where n is the length of the linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list_recursively(curr, prev):
    if curr is None:
        return prev

    next_node = curr.next
    curr.next = prev

    return reverse_list_recursively(next_node, curr)