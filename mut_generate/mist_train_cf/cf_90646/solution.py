"""
QUESTION:
Write a `get_nth_element` function that takes a linked list and an integer `n` as input, and returns the data of the nth element in the linked list. The function should not use any built-in methods or functions for accessing the elements of the linked list. If `n` is less than 1 or if the nth element does not exist, the function should return `None`.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth_element(head, n):
    if n < 1:
        return None
    current = head
    count = 1
    while current:
        if count == n:
            return current.data
        current = current.next
        count += 1
    return None