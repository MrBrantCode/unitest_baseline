"""
QUESTION:
Write a function `addTwoNumbers` that takes two linked lists representing integers as input and returns the head of a new linked list representing the sum of the input integers. The linked lists are non-empty and each node contains a single digit of the integer, with the least significant digit at the head. The function should handle cases where the sum of the input integers has more digits than the input integers.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummyHead = ListNode(0)
    p, q, curr = l1, l2, dummyHead
    carry = 0
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        sum = carry + x + y
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next
        if p: p = p.next
        if q: q = q.next
    if carry > 0:
        curr.next = ListNode(carry)
    return dummyHead.next