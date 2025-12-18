"""
QUESTION:
Create a function `printReverse` that takes an array as input and prints out all the array elements in reverse order using a doubly linked list. The doubly linked list should have methods to add a node at the end of the list and to print the array elements in reverse order. The function should return the reversed array elements.
"""

class Node:
    """Represents a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """Represents a doubly linked list."""
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        """Adds a node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def printReverse(self, array):
        """Prints out all the array elements in reverse order."""
        for data in array:
            self.addNode(data)
        
        current = self.tail
        reversed_array = []
        while current is not None:
            reversed_array.append(current.data)
            current = current.prev
        
        return reversed_array

def printReverse(array):
    """Prints out all the array elements in reverse order using a doubly linked list."""
    dll = DoublyLinkedList()
    return dll.printReverse(array)