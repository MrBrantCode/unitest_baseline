"""
QUESTION:
Write a function `deleteOccurrences(head, k)` that deletes all occurrences of a given key `k` in a singly linked list, handling cases with duplicate keys, and returns the updated linked list. The function should have a time complexity of O(n), where n is the number of nodes in the linked list, and a space complexity of O(1).
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def deleteOccurrences(head, k):
    # Check if head node needs to be deleted
    while head and head.data == k:
        temp = head
        head = head.next
        temp = None

    # Traverse the linked list
    if head is None:
        return head

    previous = head
    current = head.next
    while current:
        if current.data == k:
            # Delete current node
            previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next

    return head