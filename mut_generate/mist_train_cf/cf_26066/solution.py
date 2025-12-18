"""
QUESTION:
Write a function named `deleteNode` that takes a linked list and an integer position as input. The function should delete the node at the specified position in the linked list and modify the list accordingly. The position is 0-indexed, meaning the head of the list is at position 0. If the position is out of range or the list is empty, the function should do nothing and return.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, position):
    """
    Deletes the node at the specified position in the linked list.
    
    Args:
        head (Node): The head of the linked list.
        position (int): The position of the node to be deleted (0-indexed).
    
    Returns:
        The head of the modified linked list.
    """
    if head is None:
        return head
    
    temp = head

    if position == 0:
        head = temp.next
        return head

    for _ in range(position - 1):
        if temp is None or temp.next is None:
            return head
        temp = temp.next

    if temp.next is not None:
        temp.next = temp.next.next

    return head