"""
QUESTION:
Implement a function to create a doubly linked list of consecutive prime numbers from 2 to 29. The linked list should consist of nodes with properties for their values and references to the preceding and succeeding nodes.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def create_prime_linked_list():
    dll = DoublyLinkedList()
    for i in range(2, 30):  
        if is_prime(i):
            dll.append(i)
    return dll