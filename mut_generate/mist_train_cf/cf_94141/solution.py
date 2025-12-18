"""
QUESTION:
Write a function `hasCycle(head)` that determines whether a linked list contains a cycle. The function should have a time complexity of O(n) and use no extra space. It should return True if a cycle exists, and False otherwise. The linked list is represented as a series of nodes, each with a `val` and a `next` pointer.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True