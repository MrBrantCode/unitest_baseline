"""
QUESTION:
Implement a function `addTwoLists` that takes the head nodes of two linked lists as input, where each linked list represents a number with its digits stored in reverse order. The function should sum the corresponding nodes of the two linked lists and return the head node of a new linked list representing the sum. The function should handle carryovers and return the result with its digits also stored in reverse order.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addTwoLists(self, first, second):
    prev = Node(0)
    temp = prev
    carry = 0

    while (first is not None or second is not None):
        f_data = 0 if first is None else first.data
        s_data = 0 if second is None else second.data

        Sum = carry + f_data + s_data

        carry = 1 if Sum >= 10 else 0

        Sum = Sum if Sum < 10 else Sum % 10

        temp.next = Node(Sum)

        if first is not None:
            first = first.next
        if second is not None:
            second = second.next

        temp = temp.next

    if carry > 0:
        temp.next = Node(carry)

    return prev.next