"""
QUESTION:
Write a function named `getNthElement` that takes the head of a linked list and an integer `n` as input, and returns the data of the nth element in the linked list. If the linked list has less than n elements, the function should return -1. Assume that the linked list nodes have `data` and `next` attributes.
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

def getNthElement(head, n): 
    current = head 
    count = 0

    # looping through the linked list
    while(current is not None): 
        if (count == n-1): 
            return current.data 
        count += 1
        current = current.next
    return -1