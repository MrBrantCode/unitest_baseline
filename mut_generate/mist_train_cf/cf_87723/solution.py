"""
QUESTION:
Write a function `assign_values` that takes the head of a linked list with 4 empty nodes as input, and assigns unique values to each node in ascending order such that each node value is greater than the sum of all previous node values and the difference between each consecutive node value is at least 5. The function should return the head of the linked list with the assigned values.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def assign_values(head):
    values = [0] * 4  # Initialize an array to store the values for each node

    # Assign the values for each node
    values[0] = 1
    values[1] = values[0] + 5
    values[2] = values[1] + 5
    values[3] = values[2] + 5

    # Assign the values to the linked list nodes
    curr = head
    for i in range(4):
        curr.value = values[i]
        curr = curr.next

    return head