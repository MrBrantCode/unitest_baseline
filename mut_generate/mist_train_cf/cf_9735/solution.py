"""
QUESTION:
Implement a function `delete_first_occurrence(head, value)` that deletes the first occurrence of a given value in a singly linked list. The function should return the head of the updated linked list. The linked list node is defined as `Node(data)`, where `data` is the value stored in the node and `next` is the pointer to the next node in the list. If the value is not found in the list, the function should return the original linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_first_occurrence(head, value):
    if head is None:  
        return head
    
    if head.data == value:  
        head = head.next
        return head

    current = head
    prev = None
    
    while current.next is not None and current.data != value:
        prev = current
        current = current.next
        
    if current.data == value:  
        prev.next = current.next
    
    return head