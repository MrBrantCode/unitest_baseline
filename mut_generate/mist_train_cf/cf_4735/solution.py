"""
QUESTION:
Implement a function called `delete_nodes_with_value` that takes the head of a linked list and a target value as input and returns the head of the modified linked list with all nodes containing the target value deleted. The function should handle cases where the first node, last node, or all nodes contain the target value, and it should not use any additional data structures such as lists or dictionaries.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_nodes_with_value(head, value):
    # Handle empty list
    if head is None:
        return None
    
    # Skip any initial nodes with the target value
    while head is not None and head.data == value:
        head = head.next
    
    # Handle case when all nodes have the target value
    if head is None:
        return None
    
    prev = None
    curr = head

    while curr is not None:
        if curr.data == value:
            if prev is None:
                head = curr.next
            else:
                prev.next = curr.next
        else:
            prev = curr
        
        curr = curr.next

    return head