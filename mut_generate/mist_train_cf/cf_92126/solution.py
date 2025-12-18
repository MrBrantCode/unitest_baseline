"""
QUESTION:
Write a function `detect_cycle` that takes the head of a linked list as input and returns `True` if the linked list has a cycle, and `False` otherwise. The function must not use any additional data structures.
"""

def detect_cycle(head):
    if head is None or head.next is None:
        return False

    slow = head.next
    fast = head.next.next if head.next else None

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next if fast.next else None

    return False