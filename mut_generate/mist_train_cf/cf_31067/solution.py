"""
QUESTION:
Implement a LinkedList class with a Node class to represent a simple linked list. The LinkedList class should have methods to add a new node to the end of the list (append), print the entire list (print_list), and reverse the list (reverse). The append method should return the modified linked list after adding a new node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def entrance(data):
    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            return self

        def print_list(self):
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

        def reverse(self):
            prev = None
            current = self.head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self.head = prev

    return LinkedList()