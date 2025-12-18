"""
QUESTION:
Implement a function `removeDuplicates(head)` that removes duplicates from a sorted doubly linked list without using extra space. The function should take the head of the doubly linked list as an argument, preserve the original order of elements, and return the head of the modified linked list.
"""

class Node:  
    def __init__(self, data=None):  
        self.data = data
        self.next = None
        self.prev = None

def removeDuplicates(head):
    if head is None:
        return None
    
    curr_node = head
    next_node = head.next
    
    while next_node is not None:
        # If curr_node and next_node contains same value, then delete next node
        if curr_node.data == next_node.data:
            next_node = next_node.next
            curr_node.next = next_node
            if next_node:
                next_node.prev = curr_node
        # Otherwise, update curr_node and next_node
        else:
            curr_node = next_node
            next_node = next_node.next
                
    # Return updated head node
    return head