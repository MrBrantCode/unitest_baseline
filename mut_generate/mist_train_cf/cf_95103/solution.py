"""
QUESTION:
Write a function `deleteNode(head, val)` that deletes a node with the given value `val` from a sorted linked list in ascending order. The function should handle cases where the node to delete is the head or tail of the linked list. The function must have a time complexity of O(n), where n is the number of nodes in the linked list, and use only constant extra space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(head, val):
    if head.val == val:
        return head.next

    curr = head
    prev = None

    while curr is not None and curr.val != val:
        prev = curr
        curr = curr.next

    if curr is not None:
        if curr.next is None:
            prev.next = None
        else:
            prev.next = curr.next

    return head