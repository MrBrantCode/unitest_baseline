"""
QUESTION:
Implement a function `detectCycle(head)` that detects a cycle in a linked list and returns the starting node of the cycle. The function should take the head node of the linked list as input and return the starting node of the cycle if one exists, or `None` if there is no cycle. The linked list nodes are assumed to have a 'next' attribute pointing to the next node in the list.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def entrance(head):
    slow = head
    fast = head

    # Check if there is a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    # Reset slow pointer to head and find the starting node
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow