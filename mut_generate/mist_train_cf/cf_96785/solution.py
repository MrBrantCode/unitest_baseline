"""
QUESTION:
Create a function called `linkedListToArray` that takes the head of a singly linked list as input, where each node has a `value` and a `next` pointer. The function should return a list of node values in descending order. The linked list node can be defined as `ListNode` with an `__init__` method that initializes the node with a `value` and an optional `next` pointer.
"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def linkedListToArray(head):
    # Traverse the linked list and store the values in an array
    array = []
    current = head
    while current:
        array.append(current.value)
        current = current.next

    # Sort the array in descending order
    array.sort(reverse=True)

    return array