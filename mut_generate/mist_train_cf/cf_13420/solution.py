"""
QUESTION:
Create a function `array_to_linked_list` that takes an array as input and returns the head of a singly linked list in reverse order, without using any explicit loops.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def array_to_linked_list(arr):
    if len(arr) == 0:
        return None
    
    head = Node(arr[-1])
    head.next = array_to_linked_list(arr[:-1])
    return head