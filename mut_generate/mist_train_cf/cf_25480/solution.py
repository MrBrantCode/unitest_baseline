"""
QUESTION:
Implement a function `reverse` that takes the head of a singly linked list as input and returns the head of the reversed linked list. The function should not use any additional data structures and should be efficient in terms of space complexity.
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

def reverse(head): 
    prev = None
    current = head
    while(current is not None): 
        next = current.next
        current.next = prev 
        prev = current 
        current = next
    head = prev 
    return head