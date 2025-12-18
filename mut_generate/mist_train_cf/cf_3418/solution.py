"""
QUESTION:
Write a function `deleteNode` to delete a node with a given value from a circular linked list sorted in ascending order. The function should handle cases where the node to delete is the head or tail of the linked list, and it should have a time complexity of O(n), where n is the number of nodes in the linked list, and use constant extra space. The function should also handle cases where the linked list is empty or contains only one node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(head, value):
    """
    Deletes a node with a given value from a circular linked list sorted in ascending order.
    
    Args:
        head (Node): The head of the circular linked list.
        value (int): The value of the node to be deleted.
    
    Returns:
        Node: The head of the updated circular linked list.
    """
    if head is None:
        return head

    if head.data == value:
        if head.next == head:
            return None
        else:
            current = head
            while current.next != head:
                current = current.next
            current.next = head.next
            return current.next

    current = head
    while True:
        if current.next.data == value:
            if current.next.next == head:
                current.next = head
            else:
                current.next = current.next.next
            return head
        current = current.next
        if current == head:
            break

    return head