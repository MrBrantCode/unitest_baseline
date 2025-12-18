"""
QUESTION:
Write a function named `search_element` that takes the head node of a doubly linked list and an element as input, and returns the index of the first occurrence of the element in the list. If the element is not found, return -1. The function should iterate through the list in both forward direction using the next pointer. The index of the first node is 0.
"""

def search_element(head, element):
    current = head
    index = 0

    while current is not None:
        if current.data == element:
            return index
        current = current.next
        index += 1

    return -1