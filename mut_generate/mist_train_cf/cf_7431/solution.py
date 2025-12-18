"""
QUESTION:
Implement a function `reverse_linked_list` that takes the head of a singly linked list as input and reverses the linked list in-place without using any additional data structures. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list. The function should also handle the case where the linked list contains duplicates.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    head = prev
    return head