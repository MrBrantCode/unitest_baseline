"""
QUESTION:
Implement a function `insert_at_end` in a LinkedList class to insert a new node with the given data at the end of the linked list. The function should handle both empty and non-empty linked lists. The LinkedList class should have a Node class with a constructor that initializes the data and next pointer of the node. The LinkedList class should also have an attribute `head` to keep track of the first node in the list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def insert_at_end(self, data):
    new_node = Node(data)
        
    if self.head is None:
        self.head = new_node
        return
        
    current = self.head
    while current.next is not None:
        current = current.next
        
    current.next = new_node