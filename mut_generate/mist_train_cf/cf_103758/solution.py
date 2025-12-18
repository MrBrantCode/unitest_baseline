"""
QUESTION:
Create a function `create_linked_list` that takes a list of numbers and returns the head of a singly linked list where each node's value corresponds to an element in the input list. The function should construct the linked list in the order of the input list elements. 

Restrictions: 
- The linked list nodes should be defined using a `ListNode` class with `val` and `next` attributes.
- The `create_linked_list` function should not take any additional arguments other than the input list of numbers.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(numbers):
    head = None
    for num in numbers:
        node = ListNode(num)
        if not head:
            head = node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = node
    return head