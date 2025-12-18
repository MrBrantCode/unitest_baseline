"""
QUESTION:
Create a function named `add_linked_lists` that takes two linked lists of nodes as input, where each node contains a single digit from 0 to 9. The digits are stored in reverse order, with the head node containing the least significant digit. The function should return a new linked list representing the sum of the two input linked lists. The function should handle linked lists of different lengths, negative numbers, and cases where the sum of two digits is greater than 9, generating a carry for the next sum calculation.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def add_linked_lists(list1, list2):
    result = None
    carry = 0

    while list1 or list2:
        val1 = list1.value if list1 else 0
        val2 = list2.value if list2 else 0

        sum = val1 + val2 + carry
        carry = sum // 10
        digit = sum % 10

        if not result:
            result = Node(digit)
            current = result
        else:
            current.next = Node(digit)
            current = current.next

        if list1:
            list1 = list1.next
        if list2:
            list2 = list2.next

    if carry > 0:
        current.next = Node(carry)

    return result