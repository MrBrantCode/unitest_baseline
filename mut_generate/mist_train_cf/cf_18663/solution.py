"""
QUESTION:
Write a function named `remove_duplicates` that takes the head of a linked list as input and returns the head of the linked list with duplicates removed while maintaining the original order of elements. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if head is None:
        return head

    current = head
    unique_values = set([current.data])

    while current.next:
        if current.next.data in unique_values:
            current.next = current.next.next
        else:
            unique_values.add(current.next.data)
            current = current.next

    return head