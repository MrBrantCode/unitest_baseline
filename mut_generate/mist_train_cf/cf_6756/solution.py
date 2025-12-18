"""
QUESTION:
Write a function called `detect_loop` that takes the head of a linked list as input and returns the node at which a loop starts if a loop exists. If no loop exists, return the middle node. Assume the linked list is non-empty and the middle node is the node at the middle position if the length is odd, and the node just after the middle position if the length is even.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_loop(head: ListNode) -> ListNode:
    slow = head
    fast = head

    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Loop found, now find the node where the loop starts
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    # No loop, find middle node
    slow = head
    fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    if fast and fast.next:
        # Length of the list is even, return the node just after the middle
        return slow.next
    else:
        # Length of the list is odd, return the middle node
        return slow