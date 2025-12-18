"""
QUESTION:
Implement a function `remove_duplicates(head)` that takes the head of a linked list as input and returns the head of the modified linked list with duplicates removed. The linked list nodes contain integer values between -1000 and 1000. The function should preserve the original order of the nodes in the resulting linked list, have a time complexity of O(n), and not use any additional data structures, where n is the number of nodes in the linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head

    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head