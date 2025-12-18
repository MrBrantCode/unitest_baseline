"""
QUESTION:
Create a function `addTwoNumbers` that takes the heads of two linked lists, `l1` and `l2`, as input, where each node in the lists represents a digit in a number (most significant digit first). The function should return the head of a new linked list representing the sum of the numbers stored in `l1` and `l2`. The numbers can be of arbitrary length. The linked list nodes should have `val` and `next` attributes to store the digit value and the reference to the next node, respectively.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        curr.next = ListNode(carry % 10)
        curr = curr.next
        carry //= 10

    return dummy.next