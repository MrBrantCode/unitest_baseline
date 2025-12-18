"""
QUESTION:
Write a function `addTwoNumbers` that takes the heads of two non-empty sorted linked lists `head1` and `head2` representing non-negative integers in reverse order, with each node containing a single digit in the range [0, 9], and returns a new sorted linked list representing the sum of the two integers. The input linked lists have a maximum length of 100.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(head1, head2):
    dummy = ListNode(0)
    p = dummy
    carry = 0

    while head1 or head2 or carry:
        if head1:
            carry += head1.val
            head1 = head1.next
        if head2:
            carry += head2.val
            head2 = head2.next
        p.next = ListNode(carry % 10)
        p = p.next
        carry //= 10

    return dummy.next