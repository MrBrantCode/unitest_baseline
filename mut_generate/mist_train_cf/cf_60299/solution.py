"""
QUESTION:
Implement a function `detectCycle(head)` that takes the head of a linked list as input and returns the node where the cycle begins. If there is no cycle, return None.

The linked list nodes are represented by a class with an integer value and a next pointer to the next node. 

The function should also handle the case where the input linked list is empty or only contains one node. The time complexity should be O(N), where N is the total number of nodes in the list, and the space complexity should be O(1).
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow