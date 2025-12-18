"""
QUESTION:
Create a function called `deleteNodesWithValue` that takes two parameters: the head of a linked list (`head`) and the value to be deleted (`value`). The function should delete all nodes with the specified `value` from the linked list and return the head of the modified linked list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def deleteNodesWithValue(head, value):
    if head is None:
        return None

    while head is not None and head.value == value:
        head = head.next

    previous = head
    current = head

    while current is not None:
        if current.value == value:
            previous.next = current.next
        else:
            previous = current

        current = current.next

    return head