"""
QUESTION:
Detect Cycle in Linked List

Write a function `hasCycle(head)` that determines whether a cycle exists in a linked list. The function takes the head of the linked list as input and returns a boolean value indicating the presence of a cycle. The function should not use any additional space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def entance(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True