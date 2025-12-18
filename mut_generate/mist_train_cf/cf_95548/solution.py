"""
QUESTION:
Write a function `detect_and_remove_loop(head)` that detects a loop in a linked list and returns the starting node of the loop. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list. If there is no loop, the function should return None.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_and_remove_loop(head):
    tortoise = hare = head

    # Move hare by two steps and tortoise by one step
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next

        # If the pointers meet, there is a loop
        if hare == tortoise:
            break

    # If there is no loop
    if not hare or not hare.next:
        return None

    # Move tortoise to the head and keep hare at the meeting point
    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next

    # Find the last node of the loop
    while hare.next != tortoise:
        hare = hare.next

    # Remove the loop
    hare.next = None

    return tortoise