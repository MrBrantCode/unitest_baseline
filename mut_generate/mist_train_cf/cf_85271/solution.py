"""
QUESTION:
Write a function named `swap_adjacent_nodes` that takes the head of a doubly linked list as input, swaps the data of adjacent nodes in pairs, and returns the modified list head. The function should handle both even and odd numbers of nodes in the list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def swap_adjacent_nodes(head):
    temp = head

    while temp and temp.next:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next

    return head