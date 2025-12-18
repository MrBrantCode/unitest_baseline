"""
QUESTION:
Design a function `nth_node_from_last` that finds the nth node from the tail of a doubly-linked list. The function should not use extra space and should have a time complexity of O(n). It should not modify the given doubly-linked list. The function should handle edge cases where 'n' can be larger than the size of the list, the list is empty, or the list has a single node. It should return an error message for edge cases.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

def nth_node_from_last(self, n):
    cur = self.head
    length = self.length()
    if self.head is None:
        return "Linked List is empty"
    if n > length:
        return f"The length of the linked list is smaller than {n}"
    for i in range(length - n):
        cur = cur.next
    return cur.data