"""
QUESTION:
Write a function `assign_values` that assigns unique values to each node in a linked list of 4 nodes. Each node value must be greater than the sum of all the previous node values, and the difference between each consecutive node value should be at least 5. Return the head of the modified linked list. Assume that the linked list is already initialized with 4 empty nodes.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def assign_values(head):
    values = [0] * 4  

    values[0] = 1
    values[1] = values[0] + 5
    values[2] = values[1] + 5
    values[3] = values[2] + 5

    curr = head
    for i in range(4):
        curr.value = values[i]
        curr = curr.next

    return head