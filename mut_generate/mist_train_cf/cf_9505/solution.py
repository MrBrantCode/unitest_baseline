"""
QUESTION:
Create a function called `remove_nodes` that takes two parameters: the head of a linked list and a list of node values to be removed. The function should remove the nodes with the specified values from the linked list and return the head of the updated linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nodes(head, nodes):
    if not head:
        return head
    
    prev = None
    current = head
    while current:
        if current.val in nodes:
            if prev:
                prev.next = current.next
            else:
                head = current.next
        else:
            prev = current
        current = current.next
    
    return head