"""
QUESTION:
Create a function `reverseLinkedList` that takes the head of a linked list as input and reverses the linked list in-place without using any additional data structures or recursion. The function should have a time complexity of O(n), where n is the length of the linked list.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(head):
    if head is None or head.next is None:
        return head
    
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev