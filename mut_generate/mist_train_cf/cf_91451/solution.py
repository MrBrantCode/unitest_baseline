"""
QUESTION:
Implement a function `addTwoNumbers` that takes two linked lists `l1` and `l2` as input where each node in the linked lists contains a single digit. The function should return a new linked list representing the sum of the two input linked lists. The digits in the linked lists are stored in reverse order, meaning the ones place is at the head of the list, the tens place is at the second node, and so on. The function should handle numbers of arbitrary length and should not convert the linked lists to integers or strings.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
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