"""
QUESTION:
Implement a function `delete_first_occurrence(head, value)` that takes the head of a singly linked list and a value as input, and returns the head of the updated linked list after deleting the first occurrence of the given value. If the linked list is empty or the value is not found, return the original linked list.
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