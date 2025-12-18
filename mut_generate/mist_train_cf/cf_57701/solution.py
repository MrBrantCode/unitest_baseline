"""
QUESTION:
Write a function named `findMiddle` that takes the head of a doubly linked list as input and returns the middle element(s). If the number of elements in the list is odd, the function should return the single middle element; if the number of elements is even, the function should return the two middle elements.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def findMiddle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    if fast is not None:    # the number of elements is odd
        return slow.data
    else:                   # the number of elements is even
        return slow.prev.data, slow.data