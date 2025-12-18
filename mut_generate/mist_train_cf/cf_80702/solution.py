"""
QUESTION:
Write a function `common_elements(head1, head2)` that takes the heads of two singly linked lists as input and returns a set of their common elements. The function should have a time complexity of O(n) or better.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def common_elements(head1, head2):
    def linked_list_to_set(head):
        elements = set()
        current = head
        while current is not None:
            elements.add(current.value)
            current = current.next
        return elements

    set1 = linked_list_to_set(head1)
    set2 = linked_list_to_set(head2)
    return set1.intersection(set2)