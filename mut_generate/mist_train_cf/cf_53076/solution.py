"""
QUESTION:
Write an in-place function `reverse` that takes the head of a doubly linked list as input and reverses the list. The function should not allocate any additional space and should have a time complexity of O(n), where n is the number of nodes in the list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def reverse(head):
    temp = None
    current = head

    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    if temp is not None:
        head = temp.prev
    return head