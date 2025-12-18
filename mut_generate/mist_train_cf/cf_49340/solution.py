"""
QUESTION:
Create a function `fib` and a linked list implementation to generate the first 30 numbers in the Fibonacci series. The Fibonacci series should start with 0 and 1. The function should also be able to return the 'n'th Fibonacci number, where 'n' is the position of the number in the series starting from 0. Do not use an array data structure and instead use a linked list and recursive function methodology.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Function for adding the node at the end of a Linked List."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib(n):
    """Generate the first 'n' numbers in the Fibonacci series and return the 'n'th Fibonacci number."""
    linked_list = LinkedList()
    for i in range(n):
        linked_list.insert(fibonacci(i))
    return linked_list, fibonacci(n)