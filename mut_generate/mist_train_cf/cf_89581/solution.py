"""
QUESTION:
Write a function `detect_loop(head)` that takes the head of a linked list as input and returns the node where the loop starts if a loop exists. If there is no loop, return the middle node of the linked list. The middle node is the node at the middle position of the linked list when the length of the list is odd, and the node just after the middle position when the length is even. Assume that the linked list is singly linked and the node values are not unique.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def entrance(head: ListNode) -> ListNode:
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