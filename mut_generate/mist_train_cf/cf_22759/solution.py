"""
QUESTION:
Write a function called `reverse_list_recursively` that takes two parameters, the current node (`curr`) and the previous node (`prev`), and reverses a linked list without using any loops. The function should have a time complexity of O(n), where n is the length of the linked list.
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