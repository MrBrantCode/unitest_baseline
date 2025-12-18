"""
QUESTION:
Create a function called `addTwoNumbers` that takes two linked lists of single-digit integers as input, where each node contains a digit from 0 to 9 and the digits are stored in reverse order. The function should return a new linked list representing the sum of the two input linked lists, calculated using only the linked list representation without converting the linked lists to integers. The function should handle cases where one linked list is longer than the other.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(list1, list2):
    carry = 0
    dummy = ListNode(0)
    curr = dummy

    while list1 or list2:
        if list1:
            carry += list1.val
            list1 = list1.next
        if list2:
            carry += list2.val
            list2 = list2.next

        curr.next = ListNode(carry % 10)
        curr = curr.next
        carry = carry // 10

    if carry:
        curr.next = ListNode(carry)

    return dummy.next