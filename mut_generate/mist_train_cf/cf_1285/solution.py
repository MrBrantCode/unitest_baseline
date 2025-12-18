"""
QUESTION:
Implement a function `detectLargestCycle` to detect if a linked list contains a cycle and return the start node of the largest cycle present. The function should have a time complexity of O(n) where n is the number of nodes in the linked list and should only use a single pass through the linked list. The function should not use extra space. If there are no cycles in the linked list, the function should return None.
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

    # Step 1: Find the presence of a cycle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Step 2: Find the length of the cycle
    cycle_length = 0
    while True:
        fast = fast.next
        cycle_length += 1
        if slow == fast:
            break

    # Step 3: Find the start of the largest cycle
    slow = head
    fast = head

    # Move fast k steps ahead, where k is the length of the cycle
    for _ in range(cycle_length):
        fast = fast.next

    # Move slow and fast one step at a time until they meet again
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow