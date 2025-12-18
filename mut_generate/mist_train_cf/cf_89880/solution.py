"""
QUESTION:
Find the function `find_second_last_greater_even` that takes the head of a singly linked list and an integer `x` as input and returns the value of the second last node that is greater than `x` and even. If the linked list is empty, contains only one element, or no such node exists, return `None`. The linked list contains at most 1000 elements.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_second_last_greater_even(head, x):
    if not head or not head.next:
        return None

    if not head.next.next:
        return head.val

    prev = None
    curr = head

    while curr.next:
        if curr.next.val > x and curr.next.val % 2 == 0:
            prev = curr

        curr = curr.next

    if prev:
        return prev.val

    return None