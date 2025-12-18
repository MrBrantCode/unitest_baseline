"""
QUESTION:
Create a function called `search` that takes in the head of a singly linked list and a target entity as input, and returns a boolean indicating whether the target entity is present in the linked list. The linked list node contains an integer or string data and a next pointer. The function should iterate through the linked list and return True as soon as the target entity is found, and False otherwise. The time complexity of the function should be O(n), where n is the number of nodes in the linked list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def search(head, target):
    """
    Searches for a target entity in a singly linked list.

    Args:
    head (Node): The head of the linked list.
    target: The target entity to search for.

    Returns:
    bool: True if the target entity is found, False otherwise.
    """
    current = head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False