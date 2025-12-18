"""
QUESTION:
Function `addTwoNumbers` takes two non-empty linked lists `l1` and `l2` as input, each representing a non-negative integer where digits are stored in reverse order and each node contains a single digit. The function must return the sum of the two numbers as a linked list, without modifying the input linked lists, converting them into integers, or using additional data structures.
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