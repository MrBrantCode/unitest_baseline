"""
QUESTION:
Construct a function named `intersect` that takes two singly linked lists `set1` and `set2` as inputs and returns a new linked list containing the intersecting elements of the input lists. The intersecting elements are the values that exist in both of the input linked lists.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

def intersect(set1, set2):
    node1 = set1.head
    node2 = set2.head

    # Intersection list
    linkedlist_intersection = LinkedList()

    while node1 is not None:
        while node2 is not None:
            if node1.data == node2.data:
                linkedlist_intersection.insert(node1.data)

            node2 = node2.next
        node1 = node1.next
        node2 = set2.head
    
    return linkedlist_intersection