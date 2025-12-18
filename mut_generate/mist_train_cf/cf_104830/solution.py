"""
QUESTION:
Write a function `find_second_last_greater` that takes the head of a linked list and an integer `x` as input. The function should return the value of the second last node that is greater than `x`. If the linked list is empty or contains only one element, return `None`. If the linked list contains two elements, return the value of the first element if it is greater than `x`, otherwise return `None`.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_second_last_greater(head, x):
    if not head or not head.next:
        return None

    prev = head
    curr = head.next

    while curr.next:
        if curr.val > x:
            prev = curr
        curr = curr.next

    if prev != head:
        return prev.val

    return None