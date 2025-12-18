"""
QUESTION:
Implement the function `reverseLinkedList(head)` that takes the head of a linked list of integers as input and reverses the linked list in-place, returning the new head node. The linked list node is defined as `class ListNode: def __init__(self, val=0, next=None): self.val = val; self.next = next`. The input head node will always be valid and not None. The function should have a time complexity of O(n), where n is the number of nodes in the linked list, and should not create a new linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    curr = head
    next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev