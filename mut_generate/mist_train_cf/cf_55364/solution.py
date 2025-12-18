"""
QUESTION:
Implement a function `inject` that takes two parameters, `pos` and `data`, to inject an element `data` at a designated position `pos` in a singly linked list. The position is 0-indexed. The linked list node contains an integer or string value. The function should handle cases where the position is at the beginning, middle, or beyond the current length of the linked list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def inject(sll, pos, data):
    if pos == 0:
        new_node = Node(data)
        new_node.next = sll.head
        sll.head = new_node
    else:
        curr = sll.head
        count = 0
        while curr and count < pos:
            if count == pos - 1:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
            count += 1