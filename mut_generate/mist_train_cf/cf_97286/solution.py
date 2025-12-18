"""
QUESTION:
Implement the `reverse_list_iteratively(head)` function, which takes the head node of a singly linked list as input and returns the new head node of the reversed linked list. The function should reverse the given linked list in-place, i.e., without using any extra space, and have a time complexity of O(n), where n is the number of nodes in the linked list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list_iteratively(head):
    prev = None
    curr = head
    next_node = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev