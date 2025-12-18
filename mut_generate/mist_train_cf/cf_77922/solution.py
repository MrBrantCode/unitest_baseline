"""
QUESTION:
Design a function named `sum_two_numbers` that takes the heads of two linked lists (`llist1` and `llist2`) as input, where each node in the linked lists represents a digit in a number and the digits are ordered from most significant to least significant. The function should return the head of a new linked list representing the sum of the numbers in `llist1` and `llist2`. The numbers are non-negative and there is no leading zero in the input linked lists.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def sum_two_numbers(llist1, llist2):
    n1 = llist1.head
    n2 = llist2.head

    remainder = 0
    llist3 = LinkedList()

    while n1 is not None or n2 is not None:
        sum = remainder
        if n1 is not None:
            sum += n1.data
            n1 = n1.next
        if n2 is not None:
            sum += n2.data
            n2 = n2.next

        node = Node(sum % 10)
        remainder = sum // 10

        if llist3.head is None:
            llist3.head = node
        else:
            last = llist3.head
            while last.next:
                last = last.next
            last.next = node

    if remainder > 0:
        node = Node(remainder)
        last = llist3.head
        while last.next:
            last = last.next
        last.next = node
    return llist3