"""
QUESTION:
Write a function called `addTwoNumbers` that takes the heads of two non-empty linked lists representing two non-negative integers as input, where the digits are stored in reverse order, and each of their nodes contains a single digit. The function should add the two numbers and return the sum as a linked list. The solution must have a time complexity of O(max(m, n)) and a space complexity of O(max(m, n)), where m and n are the lengths of the input linked lists.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry:
        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next