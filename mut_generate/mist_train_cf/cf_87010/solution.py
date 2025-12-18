"""
QUESTION:
Implement a function named `search` in a circular doubly linked list class, which takes a value as input and returns the index of the first occurrence of the value in the list. If the value is not found, the function should return -1. The time complexity of the function should be O(n), where n is the number of elements in the linked list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def search(head, value):
    if head is None:
        return -1
    curr_node = head
    index = 0
    while True:
        if curr_node.value == value:
            return index
        curr_node = curr_node.next
        index += 1
        if curr_node == head:
            break
    return -1