"""
QUESTION:
Implement a recursive function `reverseList` that takes the head of a linked list as input, reverses the order of the elements in the list without using any additional data structures, and returns the head of the reversed list. The function should have a space complexity of O(1).
"""

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def reverseList(head):
    if head is None or head.next is None:
        return head

    reversed_head = reverseList(head.next)
    head.next.next = head
    head.next = None

    return reversed_head