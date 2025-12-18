"""
QUESTION:
Implement a function named `reverse_doubly_linked_list` that takes the head node of a doubly linked list as input and reverses the list in-place, with a time complexity of O(n) and without using any additional data structures.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def entance(head):
    if head is None or head.next is None:
        return head

    current = head
    while current:
        # Swap the previous and next references of the current node
        temp = current.prev
        current.prev = current.next
        current.next = temp

        # Move to the next node
        current = current.prev

    # The last node will become the new head of the reversed list
    return temp.prev if temp else None