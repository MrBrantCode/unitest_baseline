"""
QUESTION:
Create a function called `create_circular_linked_list` that generates a circular linked list containing numbers from 1 to n. The function should return a list of integers representing the data in the circular linked list. The last node in the list should point back to the first node. The function should accept an integer n as input, where n is a positive integer representing the number of nodes in the list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def display(self):
        elements = []
        cur_node = self.head
        while True:
            elements.append(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        return elements

def create_circular_linked_list(n):
    CLL = CircularLinkedList()
    for i in range(1, n+1):
        CLL.append(i)
    return CLL.display()