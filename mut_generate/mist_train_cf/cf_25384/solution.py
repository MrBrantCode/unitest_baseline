"""
QUESTION:
Create a function `add_numbers` that takes two linked lists, each representing a number with digits in reverse order, and returns a new linked list representing the sum of these two numbers. The function should handle cases where the sum of two digits is greater than 9, resulting in a carry to the next digit. The input linked lists may be of different lengths.
"""

class ListNode:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def add_numbers(list1, list2): 
    start = result = ListNode(0)
    carry = 0

    while list1 or list2 or carry: 
        val1 = 0
        val2 = 0

        if list1: 
            val1 = list1.data 
            list1 = list1.next 

        if list2: 
            val2 = list2.data 
            list2 = list2.next 

        total = val1 + val2 + carry 
        result.next = ListNode(total % 10) 
        result = result.next 
        carry = total // 10
  
    return start.next