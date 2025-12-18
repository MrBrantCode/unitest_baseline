"""
QUESTION:
Implement a function `third_last_element` that takes the head of a linked list as input and returns the value of the element positioned third from the last in the list. If the list has less than 3 elements, return "LinkedList has less than 3 elements". The function should be able to handle a singly linked list and find the solution in a single pass.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def third_last_element(head):
    first = head
    second = head
    third = head
    if head is not None:
        for i in range(2):
            if second.next is not None:
                second = second.next

        while second.next is not None:
            second = second.next
            first = third
            third = third.next

    if first:
        return first.data
    else:
        return "LinkedList has less than 3 elements"