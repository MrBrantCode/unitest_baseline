"""
QUESTION:
Write a function `reverseLinkedList` that takes the head of a singly linked list as input and returns the new head of the reversed linked list. The function should reverse the linked list in place.

The linked list node is represented by a class with a value and a next pointer. The function should not use any additional space that scales with the input size, and it should run in linear time complexity with respect to the number of nodes in the list.

The input linked list can contain between 1 and 5000 nodes.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev