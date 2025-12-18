"""
QUESTION:
Implement a function `reverseLinkedList(head)` that takes the head of a singly linked list as input and reverses the order of its nodes. The solution must have a time complexity of O(n), use constant extra space, and only modify the pointers between the nodes to reverse the order. The function should not create a new linked list, use recursion, modify the existing nodes' values, swap node values instead of actual node positions, or use any additional data structures or arrays.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev