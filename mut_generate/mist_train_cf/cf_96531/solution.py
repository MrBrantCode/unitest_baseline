"""
QUESTION:
Create a function named `addTwoNumbers` that takes two non-empty linked lists representing two non-negative integers as input. The digits are stored in reverse order, and each of their nodes contains a single digit. The function should return the sum of the two numbers as a linked list. The function should not modify the input linked lists, and it should not convert the linked lists into integers or use any built-in arithmetic operators or functions. The function should also not use recursion or any additional data structures. The time and space complexities of the function should be O(max(m, n)), where m and n are the lengths of the input linked lists.
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