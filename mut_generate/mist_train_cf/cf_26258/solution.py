"""
QUESTION:
Design a function `deleteKey` that takes the head of a singly linked list and an integer `k` as input. The function should delete all nodes in the linked list where the node's key matches the given key `k` and return the head of the updated linked list.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def deleteKey(head, k):
    """
    Deletes all nodes in the linked list where the node's key matches the given key k.

    Args:
        head (Node): The head of the singly linked list.
        k (int): The key to be deleted.

    Returns:
        Node: The head of the updated linked list.
    """
    if not head:
        return None

    if head.key == k:
        temp = head
        head = head.next
        del temp
        return deleteKey(head, k)

    curr = head
    while curr.next:
        if curr.next.key == k:
            temp = curr.next
            curr.next = curr.next.next
            del temp
        else:
            curr = curr.next

    return head