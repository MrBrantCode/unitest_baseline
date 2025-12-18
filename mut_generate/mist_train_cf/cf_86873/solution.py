"""
QUESTION:
Create a function called `detectLargestCycle` that takes the head of a linked list as input and returns the node where the largest cycle in the linked list starts. If there are multiple cycles in the linked list, the function should return the start node of the largest cycle. If the linked list does not have any cycles, the function should return `None`. The function should have a time complexity of O(n) where n is the number of nodes in the linked list, and should only make a single pass through the linked list.
"""

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def detectLargestCycle(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    has_cycle = False

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    cycle_length = 0
    while True:
        fast = fast.next
        cycle_length += 1
        if slow == fast:
            break

    slow = head
    fast = head

    for _ in range(cycle_length):
        fast = fast.next

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow