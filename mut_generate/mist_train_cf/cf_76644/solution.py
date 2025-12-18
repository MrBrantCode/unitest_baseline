"""
QUESTION:
Create a function called `RemoveDuplicates` that takes the head of a linked list of whole numbers as input, removes duplicates, sorts the remaining elements in ascending order, and returns the head of the resulting linked list. The function should not modify the original linked list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def RemoveDuplicates(head): 
    current = head;
    d_set = set()
    new_list = LinkedList()

    while current != None:
        d_set.add(current.data)
        current = current.next

    for data in sorted(d_set):
        new_list.Push(data)

    return new_list