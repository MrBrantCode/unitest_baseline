"""
QUESTION:
Write a function `addTwoNumbers` that takes two non-empty linked lists `l1` and `l2` representing two non-negative integers as input, where the digits are stored in reverse order, and each node contains a single digit. The function should add the two numbers and return the sum as a linked list. The time complexity should be O(max(m, n)), where m and n are the lengths of the input linked lists, and the space complexity should be O(1), excluding the space needed for the output linked list. The function should not modify the input linked lists, use any additional data structures, or employ recursion.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result_head = ListNode()  # Dummy node to hold the head of the result linked list
    current = result_head  # Pointer to the current node in the result linked list
    carry = 0  # Variable to hold the carry value
    
    while l1 is not None or l2 is not None:
        # Get the values of the current digits
        x = l1.val if l1 is not None else 0
        y = l2.val if l2 is not None else 0
        
        # Calculate the sum of the current digits plus the carry
        total = x + y + carry
        
        # Update the carry value
        carry = total // 10
        
        # Create a new node with the value of the sum modulo 10
        current.next = ListNode(total % 10)
        current = current.next
        
        # Move to the next nodes in the linked lists
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    
    # Check if there is still a carry value
    if carry > 0:
        current.next = ListNode(carry)
    
    return result_head.next  # Return the head node of the result linked list