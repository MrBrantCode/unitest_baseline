"""
QUESTION:
Implement a function called `delete_occurrences(head, value)` that takes the head of a singly linked list and a value to be deleted as input. The function should delete all occurrences of the given value from the linked list and return the updated linked list. The function should not use any extra space.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_occurrences(head, value):
    if head is None:
        return head

    current = head
    prev = None

    while current is not None:
        if current.value == value:
            if prev is None:
                head = current.next
            else:
                prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next

    return head