"""
QUESTION:
Write a function `addTwoNumbers` that takes two linked lists as input where each node contains a variable number of digits and the digits are stored in reverse order. The function should return the sum of the two linked lists as a new linked list in reverse order. The function should handle linked lists of different sizes.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(list1, list2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    
    while list1 or list2 or carry:
        val1 = list1.val if list1 else 0
        val2 = list2.val if list2 else 0
        
        carry, remainder = divmod(val1 + val2 + carry, 10)
        curr.next = ListNode(remainder)
        curr = curr.next
        
        list1 = list1.next if list1 else None
        list2 = list2.next if list2 else None
    
    return dummy.next