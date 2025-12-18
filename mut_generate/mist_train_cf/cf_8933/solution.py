"""
QUESTION:
Create a function `get_nth_element(n)` in a linked list class that returns the nth element of the linked list. The function should manually iterate through the linked list without using any built-in methods or functions for accessing the elements. The function should return the data of the nth node if it exists, otherwise return `None`. The input `n` is a positive integer representing the position of the node in the linked list.
"""

def get_nth_element(linked_list, n):
    if n < 1:
        return None
    current = linked_list.head
    count = 1
    while current:
        if count == n:
            return current.data
        current = current.next
        count += 1
    return None